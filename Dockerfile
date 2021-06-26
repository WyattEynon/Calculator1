FROM python3

ADD src /src

CMD [ "python", "/src/calculatorTests.py" ]