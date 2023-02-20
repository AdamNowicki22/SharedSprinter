from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    stories = data_handler.get_all_user_stories()
    return render_template('list.html', stories=stories)



@app.route('/add_story',  methods=['GET', 'POST'])
def add_story():
    if request.method == 'POST':
        title = request.form.get('title')
        user_story = request.form.get('user_story')
        acceptance_criteria = request.form.get('acceptance_criteria')
        business_value = request.form.get('business_value')
        estimation = request.form.get('estimation')
        data_handler.add_story(title, user_story, acceptance_criteria, business_value,estimation)
        return redirect(url_for('route_list'))
    return render_template('add_story.html')

@app.route('/story/<id>')
def story_id(id):
    story = data_handler.get_user_story(id)
    return render_template('story_det.html', story=story)

@app.route('/edit_story/<id>', methods=['GET', 'POST'])
def edit_story_id(id):
    story = data_handler.get_user_story(id)
    if request.method == 'POST':
        title = request.form.get('title')
        user_story = request.form.get('user_story')
        acceptance_criteria = request.form.get('acceptance_criteria')
        business_value = request.form.get('business_value')
        estimation = request.form.get('estimation')
        status = request.form.get('status')
        data_handler.edit_story(id, title, user_story, acceptance_criteria, business_value,estimation, status)
    return render_template('edit_story.html', story=story)


        # title = request.form.get('title')
        # user_story = request.form.get('user_story')
        # acceptance_criteria = request.form.get('acceptance_criteria')
        # business_value = request.form.get('business_value')
        # estimation = request.form.get('estimation')
        # status = request.form.get('status')

        # title = story[1]
        # user_story = story[2]
        # acceptance_criteria = story[3]
        # business_value = story[4]
        # estimation = story[5]
        # status = story[6]



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
