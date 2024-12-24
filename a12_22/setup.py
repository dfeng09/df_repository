from setuptools import setup, find_packages

setup(
    name='a12_22',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 在这里添加你的依赖项
    ],
    entry_points={
        'console_scripts': [
            # 如果你有命令行接口，可以在这里添加
        ]
    },
)
