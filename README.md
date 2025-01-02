# Maximizing revenue for drivers

## PROBLEM STATEMENT

In fast paced taxi booking sector, maing the most of revenue is essential for long term success and driver happiness. Our goal is to use data-driver insights to maximise revenue streams for taxi drivers in order to meet this need. Our research aims to determine whether payment methods have an impact on fare pricing by focusing on the relationship between payment type and fare amount.

## BRIEF

1. Performed `Data Exploration` and `Segmentation` to study the key characteristic features of `Payment Type` and `Trip fare` using Python.
2. Executed `Hypothesis Testing`, `Statistical Analysis`, `Anomaly Detection and Trend Analysis`, and `Feature Engineering` to identify relationship between total fare amount and payment type Customer Behavior.

## DATA DESCRIPTION

The dataset is collected from NYC.GOV - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

1. VendorID: A code indicating the TPEP provider that provided the record.
1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.

2. tpep_pickup_datetime: The date and time when the meter was engaged.

3. tpep_dropoff_datetime: The date and time when the meter was disengaged.

4. Passenger_count: The number of passengers in the vehicle.
This is a driver-entered value.

5. Trip_distance: The elapsed trip distance in miles reported by the taximeter.

6. PULo cationID: TLC Taxi Zone in which the taximeter was engaged

7. DOLocationID: TLC Taxi Zone in which the taximeter was disengaged

8. RateCodeID: The final rate code in effect at the end of the trip.
1= Standard rate
2=JFK
3=Newark
4=Nassau or Westchester
5=Negotiated fare
6=Group ride
Store_and_fwd_flag This flag indicates whether the trip record was held in vehicle
memory before sending to the vendor, aka “store and forward,”
because the vehicle did not have a connection to the server.
Y= store and forward trip
N= not a store and forward trip

9. Payment_type: A numeric code signifying how the passenger paid for the trip.
1= Credit card
2= Cash
3= No charge
4= Dispute
5= Unknown
6= Voided trip

10. Fare_amount: The time-and-distance fare calculated by the meter.Extra Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges.

11. MTA_tax: $0.50 MTA tax that is automatically triggered based on the metered rate in use.

12. Improvement_surcharge: $0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.

13. Tip_amount: Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.

14. Tolls_amount: Total amount of all tolls paid in trip.

15. Total_amount: The total amount charged to passengers. Does not include cash tips.

16. Congestion_Surcharge: Total amount collected in trip for NYS congestion surcharge.

17. Airport_fee: $1.25 for pick up only at LaGuardia and John F. Kennedy Airports


## METHODOLOGY

#### 1. Marketing Analysis.ipynb - 

#### A) Data Cleaning:

- Renamning Columns

- String Manipulations

- Missing values (Dropping the NaN as they are <1%)

- DataType Conversion

#### B) Exploratory Data Analysis (EDA):

- Outlier Analysis (Replacing with median)

- `Feature Engineering`

- `Anomaly Detection and Trend Analysis`

- `Correlation Analysis`

#### C) Performing Statistical Analysis:

- Calculating `T static` and `P-values`

- `Feature Importance (Using Random Forest)`


Finding:

1. The proportion of customers paying with cards is significantly higher than those paying with cash, with card payments accounting for 77% of all transactions compared to cash payments at
23%.
2. This indicates a strong preference among customers for using card payments over cash, potentially due to convenience, security, or incentives offered for card transactions.


#### - Amount of customers prefer to pay with card vs cash

The  proportion  of  customers  paying  with  cards  is significantly higher than those paying with cash, with card payments  accounting  for  84.5%  of  all  transactions compared to cash payments at 15.5%.

This indicates a strong preference among customers for using  card  payments  over  cash,  potentially  due  to convenience,  security,  or  incentives  offered  for  card transactions.

* T static (r):  246.53
* p-value:  0.00

We got a T-test of 152.96 and a p-value of almost zero, which states that they are statistically significant and have a positive correlation. (If the p-value is > 0.05, we will fail to reject the null hypothesis, where they do not correlate.)

#### Tip generation difference when paying with card vs cash 

The  proportion  of  customers  paying  with tips cards is slightly lesser than those paying with cash, with average tip card payments stands for  $3.188830  compared to cash payments at $3.195927.

This doesn't confirms a strong preference giving a generous tip among customers while using  card  payments  over  cashs.

* T static (r):  -0.1629398158554432 
* p-value:  0.8705951857609073

The T-statistic of -0.16 and p-value of 0.87 suggest that there is no statistically significant difference between the two groups being compared. The high p-value (> 0.05) indicates that we fail to reject the
null hypothesis which states that there is no significant difference between them.



## Recommendations

`Patterns:`
1. Encourage customers to opt for credit card payments to maximize revenue opportunities for taxicab drivers.
   
2.Implement strategies like offering incentives or discounts upto 10-15% for credit card transactions to motivate customers to choose this payment method.

3.Ensure seamless and secure credit card payment options to enhance customer convenience and promote the adoption of this preferred payment method.
