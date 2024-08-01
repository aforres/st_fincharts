import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objs as go


# Define a dictionary mapping stock names to their ticker symbols
stocks = {
    "ANZ Bank": "ANZ.AX",
    "BHP": "BHP.AX",
    "Commonwealth Bank": "CBA.AX",
    "Gold (CMX)": "GC=F",
    "National Australia Bank": "NAB.AX",
    "Oil Crude (CMX)": "CL=F",
    "Rio Tinto": "RIO.AX",
    "Silver (CMX)": "SI=F",
    "Telstra": "TLS.AX",
    "Woolworths": "WOW.AX"
}

# Page title and description
st.title('Interactive Financial Chart App')
st.write('Select a stock or commodity to view its chart:')

# Dropdown menu to select stock
selected_stock = st.selectbox('Select Instrument', list(stocks.keys()))

# Display the selected stock's name and symbol
st.write(f'Instrument selected: {selected_stock} ({stocks[selected_stock]})')

# Calculate date ranges for the last 5 years
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)  # Assuming 365 days per year

# Fetch historical data from Yahoo Finance
ticker_symbol = stocks[selected_stock]
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the data
st.write(stock_data)

# Plot the data with customized x-axis date format
#import plotly.graph_objs as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))

fig.update_layout(
    title=f'{selected_stock} Price',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_tickformat='%b %y'  # Format x-axis ticks as Day Month Year (e.g., 01 Jan 20)
)

st.plotly_chart(fig)

import streamlit as st

st.header("Excerpt from Resources Articles")

st.markdown("**Cook & Boardman Acquires B.R. Johnson, LLC**")
st.markdown("""\nFriday - August 02: (RWE) - The Cook & Boardman Group LLC ("Cook & Boardman" or "C&B"), the leading specialty distributor of commercial entry solutions and systems integration services, has announced the acquisition of B.R. Johnson, LLC ("BRJ") headquartered in Syracuse, NY. Terms of the transaction were not disclosed.
\nFounded in 1928, B.R. Johnson is a multi-location, leading distributor of windows, doors, and specialty building products, proudly serving both commercial contractors and end users throughout Central New York.
\n"We are thrilled to welcome B.R. Johnson to the Cook & Boardman family. Their expertise in a wide range of products and their talented personnel will strengthen our position in the market and drive continued growth. We are looking forward to working with Ralph, Mike, and the rest of their team to achieve even greater success in the future," said David Eisner, Chief Executive Officer of C&B.
\n"Over our nearly 100-year history, B.R. Johnson has established an impeccable reputation for selling and installing quality building products in Central New York. Our team possesses extensive industry knowledge which has allowed BRJ to establish a loyal customer base in our region." Said Ralph Corlis, President of BRJ. "We're excited to partner with Cook & Boardman to carry on BRJ's proud legacy and ensure continued success."
\nThe company will continue to operate under the B.R. Johnson name and customer contacts will remain unchanged as a result of the acquisition.
\nPlatinum Equity acquired a majority interest in Cook & Boardman in 2023. Littlejohn & Co., LLC remains a significant minority shareholder. BRJ represents C&B's sixth acquisition under Platinum Equity's ownership.
\nK&L Gates LLP served as legal advisor to Cook and Boardman. Livingstone Partners LLC served as financial advisor and Calfee, Halter & Griswold LLP as legal advisor to BRJ.
\nCook & Boardman is one of the leading specialty distributors of commercial doors, frames & hardware, electronic access control equipment and specialty (Division 10) products. The company is also one of the nation's largest and fastest growing providers of integrated security solutions - including physical security, access control, wireless networking, low voltage cabling, audio/visual and managed information technology products.
\nThe company serves non-residential and multi-family markets including the commercial, education, government, healthcare, office and hospitality sectors from more than 70 locations across 23 states and nationwide through its ecommerce portal at www.cookandboardman.com.
\n\n""")

st.divider()


st.markdown("**Flexsys To Increase Prices For Insoluble Sulfur, 6ppd And 4-adpa Products Worldwide**")
st.markdown("""\nFriday - August 02: (RWE) - Flexsys, announced it will increase prices for all Insoluble Sulfur, 6PPD and 4-ADPA products sold worldwide, effective for all shipments on or after September 1, 2024, or as customer contracts allow. The price increase will be up to 12% depending on product and world region.
\nThis price increase will help offset the effects of continued inflationary pressures on the business.
\nFurthermore, Flexsys is making significant investments in the innovation of a Next Generation Antidegradant as a replacement for 6PPD to respond to customers' requests for a more sustainable Antidegradant for tires of the future.
\nCollectively, these actions will enable Flexsys to continue to supply its customers with industry-leading products while continuing to provide world-class levels of quality, service, and reliability that Flexsys is renowned for.
\n\n""")

st.divider()


st.markdown("**Grainger Reports Results For The Second Quarter 2024**")
st.markdown("""\nFriday - August 02: (RWE) - Grainger (NYSE: GWW) today reported results for the second quarter of 2024 with sales of USD4.3 billion, up 3.1%, or 5.1% on a daily, organic constant currency basis, and adjusted diluted EPS of USD9.76, up 5.2% compared to the second quarter of 2023. 
\n"I'm proud of our team for providing a flawless experience and creating tangible value for our customers. Amidst the backdrop of a slow, but generally stable demand environment, we focused on what matters and produced another quarter of solid results," said D.G. Macpherson, Chairman and CEO. "As we look to the second half of the year, I'm confident in our ability to execute well and deliver results for all stakeholders." 
\n(1) Results exclude restructuring costs incurred in the second quarter of 2024. See the supplemental information of this release    for a reconciliation of adjusted and non-GAAP financial measures.
\nRevenueSales in the quarter, on a reported and daily basis, increased 3.1% compared to the second quarter of 2023. Normalizing for the impact of foreign currency exchange and the Company's 2023 divestiture of its subsidiary, E & R Industrial Sales, Inc., sales on a daily, organic constant currency basis increased 5.1% compared to the second quarter of 2023.
\nIn the High-Touch Solutions - N.A. segment, sales, on a reported and daily basis, were up 3.1%, or up 3.7% on a daily, organic constant currency basis, compared to the second quarter of 2023. Revenue growth for the segment was driven by increased volume in all geographies and included broad-based gains across most customer end markets. In the Endless Assortment segment, daily sales were up 3.3%, or 11.7% on a daily, constant currency basis, compared to the second quarter of 2023. Revenue growth for the segment was driven by core B2B customers at Zoro and strong performance across MonotaRO, most notably with Enterprise customers. This growth was partially offset by the continued decrease in non-core customers at Zoro.
\nGross Profit Margin: Gross profit margin of 39.3% in the second quarter of 2024 was flat to the second quarter of 2023. 
\nIn the High-Touch Solutions - N.A. segment,  2024 second quarter gross profit margin of 41.7% was flat over the prior year quarter as various factors offset in the period. In the Endless Assortment segment, gross profit margin declined by 20 basis points from the second quarter of 2023 driven primarily by product and customer mix headwinds. 
\nEarnings: For the second quarter of 2024, total company reported operating earnings were USD649 million, down 1.8% compared to the second quarter of 2023. Reported operating margin in the quarter was 15.1%, a 70-basis point decrease from the second quarter of 2023. On an adjusted basis, which removes restructuring costs incurred in the period, operating earnings for the quarter were USD665 million, up 0.6% over the second quarter of 2023. Adjusted operating margin was 15.4%, a 40 basis point decrease over the second quarter of 2023, driven by continued investment in demand-generating activities and distribution center network expansion.
\n\n""")

st.divider()

st.markdown("**MSA Safety Declares Quarterly Dividend**")
st.markdown("""\nFriday - August 02: (RWE) - The Board of Directors of MSA Safety Incorporated (NYSE: MSA) today declared a third quarter dividend of USD0.51 per share on common stock, payable September 10, 2024, to shareholders of record on August 15, 2024.
\nThe Board also declared a dividend of USD0.5625 per share on preferred stock, payable September 1, 2024, to shareholders of record on August 15, 2024.
\n\n""")

st.divider()

st.markdown("**Peabody Reports Results For Quarter Ended June 30, 2024**")
st.markdown("""\nFriday - August 02: (RWE) - Peabody (NYSE: BTU) today reported net income attributable to common stockholders of USD199.4 million, or USD1.42 per diluted share, for the second quarter of 2024, compared to USD179.2 million, or USD1.15 per diluted share in the prior year quarter.  Peabody had Adjusted EBITDA1 of USD309.7 million in the second quarter of 2024, which included USD80.8 million from an insurance settlement compared to USD358.2 million in the prior year quarter.
\n"Our operations performed safely, while achieving results in-line with expectations across all four segments.  With a strong outlook for free cash flow in the second half of 2024, we have committed USD100 million for additional share buybacks," said Peabody President and Chief Executive Officer Jim Grech.  "Development at Centurion remains on plan, with initial underground development rates exceeding expectations.  We reached first development coal in the second quarter and expect to ship to customers beginning in the fourth quarter of 2024."
\n1 Adjusted EBITDA is a non-GAAP financial measure. Adjusted EBITDA margin is equal to segment Adjusted EBITDA (excluding insurance recoveries) divided by segment revenue. Revenue per Ton and Adjusted EBITDA Margin per Ton are equal to revenue by segment and Adjusted EBITDA by segment (excluding insurance recoveries), respectively, divided by segment tons sold. Costs per Ton is equal to Revenue per Ton less Adjusted EBITDA Margin per Ton. Management believes Costs per Ton and Adjusted EBITDA Margin per Ton best reflect controllable costs and operating results at the reporting segment level. We consider all measures reported on a per ton basis, as well as Adjusted EBITDA margin, to be operating/statistical measures. Please refer to the tables and related notes herein for a reconciliation of non-GAAP financial measures.
\nPeabody expected seaborne thermal volume of 4.1 million tons, including 2.7 million export tons, at costs of USD45 to USD50 per ton.  Second quarter results were in-line with expectations, increasing segment Adjusted EBITDA margin per ton by 7.5 percent compared to the first quarter due to higher export tons.  The segment reported Adjusted EBITDA margins of 34 percent and Adjusted EBITDA of USD104.4 million.
\nPeabody expected seaborne met volume of 1.9 million tons at costs of USD110 to USD120 per ton.  Second quarter shipments were above expectations and increased 600 thousand tons compared to the first quarter following a successful longwall move at Metropolitan, which also significantly improved costs per ton.  Peabody successfully reached a USD109.5 million settlement for property loss and business disruption sustained at Shoal Creek in 2023. Peabody has included USD80.8 million in second quarter segment Adjusted EBITDA after previously reporting a USD28.7 million provision for Shoal Creek Property losses.  The segment reported Adjusted EBITDA margins of 21 percent (excluding insurance recovery) and Adjusted EBITDA of USD143.6 million.
\nPeabody expected PRB volume of 15.5 million tons at costs of USD12.75 to USD13.75 per ton.  The segment achieved costs at the low end of guidance due to continued cost containment measures.  Shipments increased as the quarter progressed, confirming expectations for higher volumes in the second half of the year.  The segment reported Adjusted EBITDA of USD17.8 million.
\nPeabody expected Other U.S. Thermal volume of 3.8 million tons at costs of approximately USD44 to USD48 per ton.  Peabody delivered 3.7 million tons at costs of USD45.53 per ton, in-line with expectations.  The segment reported Adjusted EBITDA of USD35.4 million.
\nOur world class hard coking coal growth project in Australia continues to advance on time and on budget.  We produced the first development coal in the second quarter and commissioned the second continuous miner in July.  We expect to ship first coal in the fourth quarter of 2024 and remain on track to commence longwall production in the first quarter of 2026.  Approximately USD200 million of the USD489 million of capital expenditures to reach longwall production has been completed as of June 30, 2024. 
\nCenturion is expected to have a mine life in excess of 25 years and average annual longwall production of 4.7 million tons.  The benchmark premium hard coking coal from Centurion is expected to receive a premium price relative to other metallurgical coals.  
\n\n""")

st.divider()

st.markdown("**Peabody Board Declares Dividend on Common Stock**")
st.markdown("""\nFriday - August 02: (RWE) - Peabody (NYSE: BTU) announced today that its Board of Directors has declared a quarterly dividend on its common stock of USD0.075 per share, payable on September 4, 2024 to stockholders of record on August 15, 2024.
\nPeabody is a leading coal producer, providing essential products for the production of affordable, reliable energy and steel.  Our commitment to sustainability underpins everything we do and shapes our strategy for the future.  For further information, visit PeabodyEnergy.com. 
\n\n""")

st.divider()

st.markdown("**Sigma Lithium To Release Second Quarter 2024 Results August 15, 2024**")
st.markdown("""\nFriday - August 02: (RWE) - Sigma Lithium Corporation ("Sigma Lithium" or the "Company") (NASDAQ: SGML, BVMF: S2GM34, TSXV: SGML), a leading global lithium producer dedicated to powering the next generation of electric vehicles with carbon neutral, socially and environmentally sustainable lithium concentrate announces it will release its financial results for the second quarter ended June 30, 2024 after market close on August 15, 2024. The release will be followed by an investor conference call on August 16, 2024, at 8:00am eastern time.
\nSigma Lithium's second quarter 2024 press release, investor presentation and quarterly filings will be available through the company's investor relations website, ir.sigmalithiumcorp.com. A webcast replay will also be available following the conclusion of the event.
\nABOUT SIGMA LITHIUM Sigma Lithium (NASDAQ: SGML, TSXV: SGML, BVMF: S2GM34) is a leading global lithium producer dedicated to powering the next generation of electric vehicle batteries with carbon neutral, socially and environmentally sustainable chemical-grade lithium concentrate.
\nSigma Lithium is one of the world's largest lithium producers with an annual production capacity of 270,000 tonnes of chemical grade lithium concentrate (36,700 LCE annually). The Company operates at the forefront of environmental and social sustainability in the EV battery materials supply chain at its Grota do Cirilo Operation in Brazil. The Company produces Quintuple Zero Green Lithium at its state-of-the-art Greentech lithium plant that delivers zero carbon lithium, produced with zero dirty power, zero potable water, zero toxic chemicals and zero tailings' dams.
\n\n""")

st.divider()

st.markdown("**Pan Global Announces Encouraging Soil Geochemistry Results Coincident With Bravo Gravity Target**")
st.markdown("""\nFriday - August 02: (RWE) - Pan Global Resources Inc. ("Pan Global" or the "Company") (TSXV: PGZ) (OTCQX: PGZFF) (FRA: 2EU) is pleased to announce soil geochemistry survey results for the maiden exploration program over the Bravo target ("Bravo") within the Company's 100%-owned Escacena Project ("Escacena") in the Iberian Pyrite Belt, southern Spain.
\n"The initial soil geochemistry results are very encouraging, highlighting a more-than 1km continuous lead ("Pb") plus zinc ("Zn") surface anomaly coincident with a gravity anomaly at the high-priority Bravo target. Importantly, lead and zinc commonly occur laterally or above copper-rich mineralization in zoned volcanogenic massive sulphide deposits. Based on these results, the soil geochemistry survey will now be expanded to connect with the La Romana copper-tin-silver discovery to the west," said Tim Moody, Pan Global's President & CEO.
\n"The results support our view that the large Bravo gravity anomaly could represent massive sulphide mineralization concealed beneath shallow cover sediments. A more detailed ground gravity survey at Bravo is also making good progress (30% completed) and coupled with the encouraging geochemistry results, could bring forward the timing for drilling at the Bravo target," said Mr. Moody.
\nThe soil geochemistry results reported today are for 326 soil samples, representing 57% of the planned Bravo survey. The soil samples are collected on a 40m-spacing along lines 100m apart. Each soil sample was analyzed using a hand-held x-ray fluorescence ("pXRF") device. Spatial interpretation of the pXRF results confirms a Pb plus Zn anomaly extending over 1km east-west and up to 700m north-south. Samples are ranging from 300ppm to 1,252ppm combined Pb+Zn, and individual samples reporting up to 1,115ppm Pb and 288ppm Zn. The soil anomaly is an indicator of potential deeper underlying sulphide mineralization concealed beneath post-mineral cover sediments.
\nBravo is a prominent 2km x 1.2km gravity anomaly located 1.5km east of Pan Global's La Romana copper-tin-silver discovery and 4.5km southwest of the Aznalcóllar and Los Frailes volcanogenic massive sulphide (VMS) deposits. The Bravo anomaly was originally identified from early-1980's gravity survey data and interpreted as potential concealed massive sulphide mineralization. The target is mostly covered by post-mineral rocks and sediments and has never been drill tested.
\nResults from planned soil geochemistry, gravity and IP surveys at Bravo will guide future drilling. Pan Global looks forward to updating shareholders as the Bravo exploration program progresses in the coming weeks. 
\nFurther to the July 3, 2024 media release announcing the engagement of Soar Financial to support public relations activities at the Company, the agreement specifies a monthly fee of €5,500.
\nThe soil geochemistry survey includes samples collected from the top 20cm from surface (un-sieved, weighing approx. 1kg) on a 100m x 40m grid over the gravity target area. The samples are collected in plastic bags, and a multi-element analysis obtained using an Olympus Vanta hand-held x-ray fluorescence ("pXRF") device. Analyses are repeated on 1 per 20 samples, and standards analyzed to check for deviation. Additional sample duplicates will be sent to the ALS laboratory in Seville as a further check and comparison with the pXRF results.
\n\n""")

st.divider()


st.markdown("**Pan Global Announces Encouraging Soil Geochemistry Results Coincident With Bravo Gravity Target**")
st.markdown("""\nFriday - August 02: (RWE) - Pan Global Resources Inc. ("Pan Global" or the "Company") (TSXV: PGZ) (OTCQX: PGZFF) (FRA: 2EU) is pleased to announce soil geochemistry survey results for the maiden exploration program over the Bravo target ("Bravo") within the Company's 100%-owned Escacena Project ("Escacena") in the Iberian Pyrite Belt, southern Spain.
\n"The initial soil geochemistry results are very encouraging, highlighting a more-than 1km continuous lead ("Pb") plus zinc ("Zn") surface anomaly coincident with a gravity anomaly at the high-priority Bravo target. Importantly, lead and zinc commonly occur laterally or above copper-rich mineralization in zoned volcanogenic massive sulphide deposits. Based on these results, the soil geochemistry survey will now be expanded to connect with the La Romana copper-tin-silver discovery to the west," said Tim Moody, Pan Global's President & CEO.
\n"The results support our view that the large Bravo gravity anomaly could represent massive sulphide mineralization concealed beneath shallow cover sediments. A more detailed ground gravity survey at Bravo is also making good progress (30% completed) and coupled with the encouraging geochemistry results, could bring forward the timing for drilling at the Bravo target," said Mr. Moody.
\nThe soil geochemistry results reported today are for 326 soil samples, representing 57% of the planned Bravo survey. The soil samples are collected on a 40m-spacing along lines 100m apart. Each soil sample was analyzed using a hand-held x-ray fluorescence ("pXRF") device. Spatial interpretation of the pXRF results confirms a Pb plus Zn anomaly extending over 1km east-west and up to 700m north-south. Samples are ranging from 300ppm to 1,252ppm combined Pb+Zn, and individual samples reporting up to 1,115ppm Pb and 288ppm Zn. The soil anomaly is an indicator of potential deeper underlying sulphide mineralization concealed beneath post-mineral cover sediments.
\nBravo is a prominent 2km x 1.2km gravity anomaly located 1.5km east of Pan Global's La Romana copper-tin-silver discovery and 4.5km southwest of the Aznalcóllar and Los Frailes volcanogenic massive sulphide (VMS) deposits. The Bravo anomaly was originally identified from early-1980's gravity survey data and interpreted as potential concealed massive sulphide mineralization. The target is mostly covered by post-mineral rocks and sediments and has never been drill tested.
\nResults from planned soil geochemistry, gravity and IP surveys at Bravo will guide future drilling. Pan Global looks forward to updating shareholders as the Bravo exploration program progresses in the coming weeks. 
\nFurther to the July 3, 2024 media release announcing the engagement of Soar Financial to support public relations activities at the Company, the agreement specifies a monthly fee of €5,500.
\nThe soil geochemistry survey includes samples collected from the top 20cm from surface (un-sieved, weighing approx. 1kg) on a 100m x 40m grid over the gravity target area. The samples are collected in plastic bags, and a multi-element analysis obtained using an Olympus Vanta hand-held x-ray fluorescence ("pXRF") device. Analyses are repeated on 1 per 20 samples, and standards analyzed to check for deviation. Additional sample duplicates will be sent to the ALS laboratory in Seville as a further check and comparison with the pXRF results.
\n\n""")

st.divider()

st.markdown("**Dominion Energy Announces Second-Quarter 2024 Earnings**")
st.markdown("""\nFriday - August 02: (RWE) - Dominion Energy, Inc. (NYSE: D), today announced unaudited net income determined in accordance with Generally Accepted Accounting Principles (GAAP, or reported earnings) for the three months ended June 30, 2024, of USD572 million (USD0.65 per share) compared with net income of USD583 million (USD0.67 per share) for the same period in 2023.
\nOperating earnings (non-GAAP) for the three months ended June 30, 2024, were USD563 million (USD0.65 per share), compared to operating earnings of USD310 million (USD0.35 per share) for the same period in 2023.  
\nDifferences between GAAP and operating earnings for the period include a net benefit from discontinued operations primarily associated with the sale of gas distribution operations, gains and losses on nuclear decommissioning trust funds, mark-to-market impact of economic hedging activities, and other adjustments. Details of operating earnings as compared to prior periods, business segment results and detailed descriptions of items included in reported earnings but excluded from operating earnings can be found on Schedules 1, 2, 3 and 4 of this release.
\nGuidance: The company reaffirms its full-year 2024 operating earnings guidance range of USD2.62 to USD2.87 per share. The company also reaffirms its full-year 2025 operating earnings guidance range of USD3.25 to USD3.54 per share and the other financial guidance provided at the March 1, 2024 investor meeting including guidance related to earnings, credit, and dividend.
\nWebcast today: The company will host its second-quarter 2024 earnings call at 10 a.m. ET on Thursday, Aug. 1, 2024. Management will discuss matters of interest to financial and other stakeholders including recent financial results.   
\nA live webcast of the conference call, including accompanying slides and other financial information, will be available on the investor information pages at investors.dominionenergy.com.
\nFor individuals who prefer to join via telephone, domestic callers should dial 1-800-343-1703 and international callers should dial 1-785-424-1116. The passcode for the telephonic earnings call is 40578. Participants should dial in 10 to 15 minutes prior to the scheduled start time. 
\nA replay of the webcast will be available on the investor information pages by the end of the day Aug. 1. A telephonic replay of the earnings call will be available beginning at about 1 p.m. ET on Aug. 1. Domestic callers may access the recording by dialing 1-800-839-3740.  International callers should dial 1-402-220-7239. The passcode for the replay is 40578. 
\nImportant note to investors regarding operating, reported earningsDominion Energy uses operating earnings (non-GAAP) as the primary performance measurement of its results for public communications with analysts and investors. Operating earnings are defined as reported earnings adjusted for certain items. Dominion Energy also uses operating earnings internally for budgeting, for reporting to the Board of Directors, for the company's incentive compensation plans, and for its targeted dividend payouts and other purposes. Dominion Energy management believes operating earnings provide a more meaningful representation of the company's fundamental earnings power.
\n\n""")

st.divider()
