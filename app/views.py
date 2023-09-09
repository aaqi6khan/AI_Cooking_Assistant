from flask import render_template, request
from app import app
from .query_data import get_food_list
from .serpapi import get_info


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def collect_form_info():
    # Get the user's answers from the form
    ingredients = request.form.get('ingredients')
    cuisine = request.form.get('cuisine')
    dietrypreference = request.form.get('dietrypreference')
    skilllevel = request.form.get('skilllevel')
    spicelevel = request.form.get('spicelevel')
    time = request.form.get('time')
    allergies = request.form.get('allergies')


    # Execute the logic to generate gift ideas based on the keywords
    keywords = get_food_list(ingredients, cuisine, dietrypreference, skilllevel, spicelevel, time, allergies)  
    # Query SERPAPI for each keyword and compile the results
    Dishes = []
    for keyword in keywords:
        serpapi_results = get_info(keyword)
        for result in serpapi_results:
            khana = {
                "Dish": keyword, 
                "title": result.get('title', 'N/A'), 
                "link": result.get('link', 'N/A'), 
                "snippet": result.get('snippet', 'N/A'), 
                "thumbnail": result.get('thumbnail', 'N/A')
            }
            Dishes.append(khana)

    # Render the template with the results
    return render_template('results.html',Dishes=Dishes)