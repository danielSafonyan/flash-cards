import io

with open("logs.txt", "a", encoding="utf-8") as logger:

    for i in range(3):
        logger.write(f'Log number: {i + 1}\n')