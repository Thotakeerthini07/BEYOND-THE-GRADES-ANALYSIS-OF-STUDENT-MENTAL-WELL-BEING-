import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\Sriram\OneDrive\Desktop\Analysis of Student Mental Wellbeing\Depression Student Dataset.csv")


# Preprocessing
df['Depression'] = df['Depression'].map({'Yes': 1, 'No': 0})
df['Family History of Mental Illness'] = df['Family History of Mental Illness'].map({'Yes': 1, 'No': 0})
df['Dietary Habits'] = df['Dietary Habits'].map({'Unhealthy': 1, 'Moderate': 2, 'Healthy': 3})
df['Have you ever had suicidal thoughts ?'] = df['Have you ever had suicidal thoughts ?'].map({'Yes': 1, 'No': 0})

# --- Define the 22 Figures Based on Your Analysis ---

fig1 = px.bar(df.groupby(['Gender', 'Depression']).size().reset_index(name='Count'),
              x='Gender', y='Count', color='Depression', title='Depression by Gender')

fig2 = px.pie(df.groupby(['Family History of Mental Illness', 'Depression']).size().reset_index(name='Count'),
              names='Family History of Mental Illness', values='Count',
              title='Family History vs. Depression', hole=0.4)

fig3 = px.bar(df.groupby(['Dietary Habits', 'Depression']).size().reset_index(name='Count'),
              x='Dietary Habits', y='Count', color='Depression', title='Depression by Dietary Habits')

fig4 = px.line(df.groupby(['Academic Pressure', 'Depression']).size().reset_index(name='Count'),
               x='Academic Pressure', y='Count', color='Depression', title='Academic Pressure vs. Depression')

fig5 = px.box(df, x='Depression', y='Financial Stress', color='Depression',
              title='Financial Stress vs. Depression', points='all')

fig6 = px.density_heatmap(df.groupby(['Gender', 'Financial Stress', 'Academic Pressure', 'Dietary Habits',
                                      'Family History of Mental Illness'])['Depression'].count().reset_index(name='Count'),
                          x='Gender', y='Financial Stress', z='Count',
                          facet_col='Academic Pressure', facet_row='Family History of Mental Illness',
                          title='Demographic Heatmap vs Depression')

fig7 = px.bar(df.groupby("Study Hours")["Study Satisfaction"].mean().reset_index(),
              x="Study Hours", y="Study Satisfaction", color="Study Satisfaction",
              title="Avg Study Satisfaction for Different Study Hours")

fig8 = px.bar(df.groupby(['Study Hours', 'Depression']).size().reset_index(name='Count'),
              x='Study Hours', y='Count', color='Depression', title="Study Hours vs Depression")

fig9 = px.pie(df.groupby(['Study Satisfaction', 'Depression']).size().reset_index(name='Count'),
              names='Study Satisfaction', values='Count', color='Depression', hole=0.4,
              title="Study Satisfaction vs Depression")

fig10 = px.bar(df.groupby("Sleep Duration")["Have you ever had suicidal thoughts ?"].sum().reset_index(),
               x="Sleep Duration", y="Have you ever had suicidal thoughts ?",
               title="Suicidal Thoughts vs Sleep Duration")

fig11 = px.box(df, x='Have you ever had suicidal thoughts ?', y='Sleep Duration', color='Have you ever had suicidal thoughts ?',
               title="Sleep Duration vs Suicidal Thoughts")

fig12 = px.bar(df.groupby("Sleep Duration")["Depression"].mean().reset_index(),
               x="Sleep Duration", y="Depression", color="Depression",
               title="Impact of Sleep Duration on Depression")

fig13 = px.bar(df, x='Sleep Duration', color='Dietary Habits', barmode='stack',
               title='Sleep Duration vs Dietary Habits')

fig14 = px.line(df.groupby(['Sleep Duration', 'Academic Pressure']).size().reset_index(name='Count'),
                x='Sleep Duration', y='Count', color='Academic Pressure',
                title='Sleep Duration vs Academic Pressure')

diet_depression_counts = depressed_df['Dietary Habits'].value_counts().reset_index()
diet_depression_counts.columns = ['Dietary Habits', 'Count']

fig15 = px.pie(
    diet_depression_counts,
    names='Dietary Habits',
    values='Count',
    title='Diet Habits of Depressed Students'
)


fig16 = px.density_heatmap(df.groupby(['Study Satisfaction', 'Depression']).size().reset_index(name='Count'),
                           x='Study Satisfaction', y='Depression', z='Count',
                           title='Study Satisfaction vs Depression (Heatmap)')

fig17 = px.scatter(df.groupby(['Study Hours', 'Depression', 'Study Satisfaction']).size().reset_index(name='Count'),
                   x='Study Hours', y='Study Satisfaction', size='Count', color='Depression',
                   title='Study Hours vs Study Satisfaction vs Depression')

fig18 = px.density_heatmap(df.groupby(['Sleep Duration', 'Have you ever had suicidal thoughts ?']).size().reset_index(name='Count'),
                           x='Sleep Duration', y='Have you ever had suicidal thoughts ?', z='Count',
                           title='Sleep Duration vs Suicidal Thoughts (Heatmap)')

fig19 = px.bar(df.groupby(['Financial Stress', 'Academic Pressure']).size().reset_index(name='Count'),
               x='Financial Stress', y='Count', color='Academic Pressure',
               title='Financial Stress vs Academic Pressure')

fig20 = px.scatter_3d(df.dropna(subset=['Age', 'Study Hours', 'Academic Pressure', 'Study Satisfaction', 'Depression']),
                      x='Age', y='Study Hours', z='Academic Pressure', size='Study Satisfaction',
                      color='Depression', title='3D Scatter Plot of Depression Analysis')

fig21 = px.scatter_ternary(df, a='Study Hours', b='Financial Stress', c='Academic Pressure',
                           hover_name="Gender", color="Gender", size="Age", title='Ternary Plot: Study vs Stress vs Pressure')

# For fig22, create any additional chart or reuse one if not specified
fig22 = fig1  # Placeholder or reuse any meaningful chart

# --- Dash App Setup ---
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('"Analysis of Student Mental Well-Being"', style={'textAlign': 'center', 'color': colors['text']}),
    html.Div('-KEERTHINI THOTA', style={'textAlign': 'center', 'color': colors['text']}),

    *[dcc.Graph(id=f'firstgraph{i}', figure=eval(f'fig{i}'),
                style={'width': '80%', 'display': 'inline-block', 'backgroundColor': colors['background']})
      for i in range(1, 23)]
])

if __name__ == '__main__':
    app.run(debug=True)

