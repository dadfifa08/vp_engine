from flask import render_template
from dashboard import routes
from utils.analytics import Analytics

analytics = Analytics()

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/admin')
def admin():
    return render_template('admin.html')

@routes.route('/stats')
def stats():
    data = analytics.fetch_stats()
    return render_template('stats.html', stats=data)
