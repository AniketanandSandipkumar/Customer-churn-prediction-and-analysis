import pandas as pd
import plotly.express as px
import os

# --- Load your dataset ---
df = pd.read_csv("customer_churn_dataset.csv")  # change path if needed

# Ensure target folder exists
os.makedirs("static/plots", exist_ok=True)

# --- 1️⃣ Churn Rate Distribution ---
fig1 = px.pie(df, names='Churn', title='Churn Rate Distribution', hole=0.4,
              color_discrete_sequence=['#66fcf1', '#45a29e'])
fig1.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig1.write_html("static/plots/churn_distribution.html", include_plotlyjs='cdn')

# --- 2️⃣ Churn by Gender ---
fig2 = px.bar(df.groupby('Gender')['Churn'].mean().reset_index(),
              x='Gender', y='Churn', color='Gender',
              title='Churn Rate by Gender', text='Churn',
              color_discrete_sequence=['#66fcf1', '#45a29e'])
fig2.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig2.write_html("static/plots/churn_by_gender.html", include_plotlyjs='cdn')

# --- 3️⃣ Churn by Subscription Type ---
fig3 = px.bar(df, x='Subscription Type', color='Churn',
              barmode='group', title='Churn by Subscription Type',
              color_discrete_sequence=['#66fcf1', '#45a29e'])
fig3.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig3.write_html("static/plots/churn_by_subscription.html", include_plotlyjs='cdn')

# --- 4️⃣ Churn by Contract Length ---
fig4 = px.bar(df, x='Contract Length', color='Churn',
              barmode='group', title='Churn by Contract Length',
              color_discrete_sequence=['#66fcf1', '#45a29e'])
fig4.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig4.write_html("static/plots/churn_by_contract.html", include_plotlyjs='cdn')

# --- 5️⃣ Tenure vs Churn ---
fig5 = px.box(df, x='Churn', y='Tenure', color='Churn',
              title='Tenure vs Churn', color_discrete_sequence=['#66fcf1', '#45a29e'])
fig5.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig5.write_html("static/plots/tenure_vs_churn.html", include_plotlyjs='cdn')

# --- 6️⃣ Support Calls vs Churn ---
fig6 = px.box(df, x='Churn', y='Support Calls', color='Churn',
              title='Support Calls vs Churn', color_discrete_sequence=['#66fcf1', '#45a29e'])
fig6.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig6.write_html("static/plots/support_vs_churn.html", include_plotlyjs='cdn')

# --- 7️⃣ Payment Delay vs Churn ---
fig7 = px.box(df, x='Churn', y='Payment Delay', color='Churn',
              title='Payment Delay vs Churn', color_discrete_sequence=['#66fcf1', '#45a29e'])
fig7.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig7.write_html("static/plots/payment_delay_vs_churn.html", include_plotlyjs='cdn')

# --- 8️⃣ Total Spend by Subscription Type ---
fig8 = px.bar(df, x='Subscription Type', y='Total Spend', color='Subscription Type',
              title='Total Spend by Subscription Type',
              color_discrete_sequence=['#66fcf1', '#45a29e', '#c5c6c7'])
fig8.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig8.write_html("static/plots/total_spend_by_subscription.html", include_plotlyjs='cdn')

# --- 9️⃣ Average Spend by Churn Status ---
avg_spend = df.groupby('Churn')['Total Spend'].mean().reset_index()
fig9 = px.bar(avg_spend, x='Churn', y='Total Spend', color='Churn',
              title='Average Spend by Churn Status', text='Total Spend',
              color_discrete_sequence=['#66fcf1', '#45a29e'])
fig9.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig9.write_html("static/plots/avg_spend_by_churn.html", include_plotlyjs='cdn')

# --- 🔟 Age Distribution by Churn ---
fig10 = px.histogram(df, x='Age', color='Churn', marginal='box', nbins=20,
                     title='Age Distribution by Churn',
                     color_discrete_sequence=['#66fcf1', '#45a29e'])
fig10.update_layout(
    plot_bgcolor='#fff4eb',
    paper_bgcolor='#fff1e6',
    font=dict(color='#3b2f2f', family='Poppins', size=14),
    title_font=dict(size=18, color='#2d1f1f', family='Poppins'),
    margin=dict(l=60, r=40, t=80, b=60)
)
fig10.write_html("static/plots/age_distribution_by_churn.html", include_plotlyjs='cdn')

print("All 10 Plotly visualizations generated and saved in static/plots/")
