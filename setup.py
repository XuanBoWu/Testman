from setuptools import setup, find_packages

setup(
    name='testman',  # 项目名称
    version='0.1.0',               # 项目版本
    packages=find_packages(),       # 自动找到所有包
    entry_points={
        'console_scripts': [
            'tm=testman.cli.tm:main',     # 命令行入口点
        ],
    },
    install_requires=[],            # 安装所需的依赖库
    python_requires='>=3.6',        # Python 版本要求
    description='A simple command line tool',  # 项目描述
    long_description=open('README.md').read(),  # 详细描述可以从 README 文件读取
    long_description_content_type='text/markdown',  # 内容格式
    classifiers=[
        'Programming Language :: Python :: 3',  # Python 版本
        'License :: OSI Approved :: MIT License',  # 许可证
        'Operating System :: OS Independent',      # 支持的操作系统
    ],
    url='https://github.com/yourusername/my_command_line_tool',  # 项目主页或代码库
    author='Wu XuanBo',           # 作者
    author_email='wuxuanbo@foxmail.com',  # 作者邮箱
)