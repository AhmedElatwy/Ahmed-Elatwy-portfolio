# Social Media Emotions Analysis

A data analysis project exploring how daily social media usage time, posts, likes, comments, and messages relate to user emotions (e.g., Happiness, Anxiety, Boredom). Built with Python, Pandas, Seaborn, and Matplotlib.

## Key Insights
- Happiness correlates with high usage (~160 min/day) and engagement (e.g., 7-8 posts/day, 100 likes/day), especially on Instagram.
- Anxiety drives messaging (~30-40/day) and longer sessions on WhatsApp.
- Boredom leads to low activity across platforms.

![Usage Time by Emotion](https://github.com/AhmedElatwy/Social-Media-Emotions/blob/615738e9d56563a8a3d9bb3c3501a9854693c662/Charts/Daily%20usage%20vs%20emotion.png)

## Methodology
- Data cleaning and exploration with Pandas.
- Visualizations: Boxplots and bar charts for trends by gender/platform.
- Insights derived from averages, correlations, and breakdowns.

## Presentation
View the full slides: [presentation/project_presentation.pdf](https://github.com/AhmedElatwy/Social-Media-Emotions/blob/33b37f26e752b147d59a2ca8340856034d14c613/Social%20Media%20Emotion.pdf)

## Challenges Overcome
- Cleaned data with `df.fillna()` and `winsorize()` to handle outliers in Likes_Received_Per_Day.
- Refined `sns.boxplot()` visuals with `plt.figure(figsize=(12,6))` for better readability.
- Analyzed platform trends using `df.groupby('Platform')['Daily_Usage_Time'].mean()` to explain emotional variances.
- Fixed Switched data in 'age' and 'gender' columns using df.loc()

## Acknowledgments
- Inspired by real-world social media trends.
- Tools: Python ecosystem for analysis.
