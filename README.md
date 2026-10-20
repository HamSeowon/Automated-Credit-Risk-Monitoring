# Automated-Credit-Risk-Monitoring

A Probability of Default (PD) model for mortgage loans—trained on data from 2005–2017—is subjected to automated monthly monitoring using data from 2018–2025. This process is designed to detect events such as the impact of the COVID-19 pandemic and the subsequent recovery as the pandemic subsided.
- Data: Freddie Mac loan data; FRED macroeconomic data (unemployment rates, interest rates).
- Model: Logistic regression-based PD model.
- Monitoring: Population Stability Index (PSI) for individual variable scores; delinquency rates and loan forbearance/deferral rates for existing portfolios; the Sahm Rule.
  - Key questions: Have the borrower profiles shifted? Are actual defaults or issues emerging? Has the economy taken a downturn?
- Automation: To be implemented with the assistance of AI....

Goal
Build an automated system that monitors a mortgage PD model month by month, and test whether it can detect the COVID-19 shock through drift, delinquency, and macroeconomic signals.

Personal Motivation
I wanted to deepen my understanding of how the economy and financial systems interact. By training a model on historical data and replaying it against events whose outcomes are already known, I can test whether an automated monitoring system would have actually worked in real time.
