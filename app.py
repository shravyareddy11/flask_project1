from flask import Flask

FAI=Flask(__name__)


@FAI.route('/first')
def first():
    return('Hello Flask')


if __name__=='__main__':
    FAI.run(debug=True)

