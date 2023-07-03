# 指定基础镜像
FROM continuumio/miniconda3:latest as builder

# 设置工作目录
WORKDIR /app

# 复制 environment.yml 文件到容器中
COPY environment2.yml /app/environment2.yml

# 复制 myapp 文件夹到容器中
COPY myapp /app/myapp

# 复制 first_project 文件夹到容器中
COPY first_project /app/first_project

# 复制 start.sh 文件到容器中
COPY start.sh /app/start.sh

COPY manage.py /app/manage.py
# 创建 Conda 环境并安装依赖项
RUN conda env create -f environment2.yml --name djE2

# 安装 Pip 依赖项
RUN /bin/bash -c "conda run -n djE2 pip install --no-cache-dir -r /app/myapp/requirements.txt"

# Run stage
FROM continuumio/miniconda3:latest

WORKDIR /app

# 从builder阶段复制已安装的依赖和项目文件
COPY --from=builder /opt/conda/ /opt/conda/
COPY --from=builder /app .

# 设置环境变量
ENV DJANGO_SETTINGS_MODULE=first_project.settings

# 暴露运行端口（如果 Django 应用程序监听了特定端口）
EXPOSE 8000

# 运行 Django 项目
CMD ["bash", "/app/start.sh"]