import streamlit as st
from src.components.data_ingesion import DataInsgest
from src.pipeline.transformation_pipeline import DataTransformationPipe

data, matches, tables = DataInsgest().initiate_ingesion()
all_teams = data['Batting'].unique()
all_venues = data['City'].unique()

with st.form('submit form'):

    col1, col2 = st.columns(2)
    batting_team = col1.selectbox(':green[Batting team]', all_teams)
    bowling_team = col2.selectbox(':red[Bowling team]', all_teams)
    host = st.selectbox(':blue[City]', all_venues)

    col3, col4, col5, col6 = st.columns(4)
    total_run = col6.number_input('Target run')
    score = col3.number_input('Score')
    overs = col4.number_input('Over')
    wicket = col5.number_input('Wicket out')

    submit = st.form_submit_button('Submit')
    if submit:
        if total_run > 0 and score > 0 and total_run > score:
            runs_left = total_run - score
            balls_left = 120 - (overs*6)
            wicket_left = 10 - wicket
            crr = score/overs
            rrr = (runs_left*6)/balls_left
            input_data = {
                'Batting': [batting_team],
                'Bowling': [bowling_team],
                'City': [host],
                'Runs_left': [runs_left],
                'Balls_left': [balls_left],
                'Wicket_left': [wicket_left],
                'Total_run': [total_run],
                'crr': [crr],
                'rrr': [rrr]
            }
            predicted = DataTransformationPipe().predict_result(input_data)
            st.header(batting_team + ' ' + str(predicted[0][0]) + '%')
            st.header(bowling_team + ' ' + str(predicted[0][1]) + '%')


