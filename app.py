from flask import Flask, render_template
from config import Config

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')

#导入配置文件
# app.config.from_pyfile('config.cfg')

# app.config.from_object(Config)
# app.debug=True


@app.route('/')
def index():

    return render_template('index.html', name='index')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
