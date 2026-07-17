L2='#6a1b9a'
L1='#f3e5f5'
L0='#2e7d32'
K_='#3949ab'
Kz='#e8eaf6'
Ky='180 Days'
Kx='90 Days'
Kw='Newest First'
Kv='Today Only'
Ku='Past 7 Days'
Kt='540222'
Ks='532480'
Kr='532209'
Kq='513377'
Kp='500420'
Ko='540175'
Kn='502525'
Km='500260'
Kl='508869'
Kk='532488'
Kj='524715'
Ki='500209'
Kh='DALMIA'
Kg='APOLLOHOSP'
Kf='SUNPHARMA'
Ke='lower limit'
Kd='upper limit'
Kc='title_raw'
Kb="\n            function(params) {\n                let v = String(params.value).toLowerCase();\n                if (v.includes('strong uptrend') || v.includes('bullish') || v.includes('strong buy')) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (v.includes('uptrend') || v.includes('buy') || v.includes('high') || v.includes('yes')) return { 'backgroundColor': '#a5d6a733', 'color': '#000' };\n                if (v.includes('sideways') || v.includes('watch') || v.includes('normal')) return { 'backgroundColor': '#f4b40033', 'color': '#000' };\n                if (v.includes('bearish') || v.includes('avoid') || v.includes('low') || v.includes('downtrend')) return { 'backgroundColor': '#ea433533', 'color': '#000' };\n                return null;\n            }\n            "
Ka="\n            function(params) {\n                let val = parseFloat(params.value);\n                if (val >= 75) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 55) return { 'backgroundColor': '#f4b40033', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 35) return { 'backgroundColor': '#ff990033', 'color': '#000' };\n                return { 'backgroundColor': '#ea433533', 'color': '#000' };\n            }\n            "
KZ='Automatically adjust column widths based on text length of the selected row.'
KY=' (100%)'
KX='Other Assets (unspecified)'
KW='Cash & Equivalents'
KV='#00897b'
KU='Trade Receivables'
KT='Inventory'
KS='#5e35b1'
KR='Fixed Assets / Net PPE'
KQ='#5c6bc0'
KP='#8d6e63'
KO='Trade Payables'
KN='Total Debt'
KM='Reserves'
KL='Equity Capital'
KK='gauge+number'
KJ='institutional'
KI='institutional %'
KH='delivery %'
KG='Last Close'
KF='rgba(0,0,0,0.08)'
KE='RSI(14)'
KD='system-ui, sans-serif'
KC='rgba(0,0,0,0.06)'
KB='#31333F'
KA='tonexty'
K9='circle'
K8='#EF6C00'
K7='top right'
K6='#7C3AED'
K5='#FFD600'
K4='Candle'
K3='%d %b %Y %H:%M'
K2='⚠️ No AI configured. Add `GEMINI_API_KEY` or `GROQ_API_KEY` to Streamlit secrets.'
K1='stock name'
K0='company name'
J_='Type symbol name...'
Jz='Search symbol:'
Jy='Stocks'
Jx='%{customdata}: %{y:.2f}%<extra></extra>'
Jw='displaylogo'
Jv='#e3f2fd'
Ju='%Y%m%d_%H%M'
Jt='52w low date'
Js='52w high date'
Jr='Market Cap'
Jq='RONW %'
Jp='Face Value'
Jo='Institutional %'
Jn='Promoters %'
Jm='50 DMA < 200 DMA'
Jl='50 DMA > 200 DMA'
Jk='50 DMA > 100 DMA > 200 DMA'
Jj='50 DMA < 100 DMA < 200 DMA'
Ji='All (No Filter)'
Jh='macd crossover'
Jg='start gtt order'
Jf='output'
Je='🎨 Custom Hex: '
Jd='#ff9900'
Jc='#f4b400'
Jb='bf_search'
Ja='perf_matrix_search'
JZ='main_matrix_search'
JY='search_query'
JX='50 dma'
JW='d/e ratio'
JV='52w low'
JU='vol_val'
JT='percent'
JS='official nse'
JR='market smith'
JQ='chartlink'
JP='zerodha'
JO='screener'
JN='history data'
JM='trading view'
JL='1ayxuNlYGuJ0FKKCb7RoRL90ifwsAAx2aN6mmhO-37P8'
JK='https://www.googleapis.com/auth/drive'
JJ='https://spreadsheets.google.com/feeds'
JI="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; font-family: system-ui, -apple-system, sans-serif;'>"
JH='Output'
JG='Price %'
JF='GROQ_API_KEY'
JE='GEMINI_API_KEY'
Gt='concalls'
Gs='credit_ratings'
Gr='annual_reports'
Gq='announcements'
Gp='1 Year'
Go='30 Days'
Gn='total assets'
Gm='net ppe'
Gl='fixed assets'
Gk='trade payables'
Gj='trade receivables'
Gi='cash equivalent'
Gh='cash and equiv'
Gg='cash & equiv'
Gf='inventory'
Ge='total debt'
Gd='reserves'
Gc='total equity capital'
Gb='Sector'
Ga='rgba(0,0,0,0.3)'
GZ='#FF5252'
GY='#00E676'
GX='type'
GW='#D50000'
GV='#00C853'
GU='🚨 **[ALERT]** '
GT='Recent'
GS='Grade'
GR='Strategy'
GQ='% Gain'
GP='Target'
GO='last_pine_result'
GN='last_ai_result'
GM='100%'
GL='streamlit'
GK='Default'
GJ='📏 Column Width Adjustment:'
GI='Difference from 200 DMA column not detected for this sheet.'
GH='#fff8e1'
GG='#1b5e20'
GF='market cap'
GE='close price'
GD='high'
GC='low'
GB='buy signal'
GA='trend'
G9='breakout signal'
G8='volume trend'
G7='industry'
G6='52w_low'
G5='52w_high'
G4='Watchlist'
G3='% delivery'
G2='pledged'
G1='pledged %'
G0='promoter'
F_='promoters %'
Fz='200 dma'
Fy='#ef5350'
Fx='Error'
Fw='Loading...'
Fv='⚡ Groq (Fast)'
Fu=getattr
Ft=TypeError
EW='ppt'
EV='#9e9e9e'
EU='#FFFFFF'
ET='system-ui, -apple-system, sans-serif'
ES='skip'
ER='lines'
EQ='Low'
EP='High'
EO='locked in circuit'
EN='hits circuit'
EM='lower circuit'
EL='upper circuit'
EK='52-week low'
EJ='52-week high'
EI='%d %b %Y'
EH='Use Case'
EG='% Risk'
EF='Type'
EE='model'
ED='markers'
EC='dash'
EB='sector'
EA='atr_approx'
E9='Added On'
E8='BF Grade'
E7='net sales'
E6='net profit'
E5='Pct_Change'
E4='value'
E3='stock'
E2='stock symbol'
E1='ticker'
E0='<[^>]*>'
D_='gcp_service_account'
Dz='No Data'
Dy=range
Dx=enumerate
DM='#c62828'
DL='dot'
DK='.//item'
DJ='result'
DI='sym'
DH='left'
DG='% Diff from 200 DMA'
DF='N/A'
DE='#b71c1c'
DD='openpyxl'
DC='trail_sl_50dma'
DB='52 week high'
DA='added'
D9='BF Score'
D8='Note'
D7='Turnover'
D6='id'
D5='nse code'
D4='#ffffff'
D3='</div>'
D2='#66bb6a'
Cg='#37474f'
Cf='Mozilla/5.0'
Ce='User-Agent'
Cd='✅✅ Fit to Row 2'
Cc='✅ Fit to Row 1'
Cb='<br>'
Ca='#e8f5e9'
CZ='52'
CY='bf_score'
CX='52 week low'
CW='Value'
CV='price %'
CU='%Y-%m-%d %H:%M:%S'
CT='-%'
CS='+%'
CR='+Diff @ 200 DMA'
CQ='-Diff @ 200 DMA'
CP='Final List 2'
CO='Final List'
Bz='rgba(0,0,0,0.2)'
By='Arial Black, Arial, sans-serif'
Bx='snap'
Bw='Buy Signal'
Bv='MACD Crossover'
Bu='Trend'
Bt='Breakout Signal'
Bs='Volume Trend'
Br='_'
Bq='📱 If frame is blank on mobile, tap the link above to open directly.'
Bp='#ffebee'
Bo='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
Bn='%Y%m%d'
Bm='bf_grade'
Bl='turnover'
BQ='UTC'
BP='RSI (14)'
BO='Price (₹)'
BN='note'
BM='delivery'
BL='volume'
BK='[%,]'
BJ='Close'
BI='NSE Fundamentals'
BH='NSE Price Data'
B7='Diff. from 200 DMA'
B6='gray'
B5='#f9a825'
B4='price'
B3=isinstance
Au='#0a1758'
At='pubDate'
As='date'
Ar=1.
Aq='52W Low'
Ap='52W High'
Ao='% Delivery'
Ah='sec'
Ag='hour'
Af='min'
Ae='#16e37f'
Ad='symbol'
Ac='_txt_'
Ab='_bg_'
Aa=any
AZ=ValueError
AU='bold'
AT='normal'
AS='#ea4335'
AR='None'
AQ='coerce'
AP='CMP'
AO=list
AK='timestamp'
AJ='Just now'
AG='#1565C0'
AF='display_title'
AE=','
AD=max
A9='title'
A8='nan'
A3='cmp'
A2='change'
A0='#0f9d58'
u='plotly_white'
t='%'
s='Volume'
o='_raw_symbol_'
l='-'
j='Symbol'
i=.0
g=Exception
f='link'
c='---'
b=round
U=int
S=len
R=next
M=float
L='time_ago'
J=False
G=str
E=dict
D=None
C=''
B=True
import streamlit as A,pandas as H,numpy as AA,gspread as EX
from google.oauth2.service_account import Credentials as Gu
from google.auth.transport.requests import AuthorizedSession as L3
import json as EY,urllib.parse
from datetime import datetime as m
from st_aggrid import AgGrid as EZ,GridOptionsBuilder as Ea,JsCode as B8
from st_aggrid.shared import GridUpdateMode as L4
import streamlit.components.v1 as Q,re,io,google.generativeai as Gv,plotly.graph_objects as P
from plotly.subplots import make_subplots as L5
A.set_page_config(page_title='NF-750-Delivery % (+V)',layout='wide',page_icon='📊')
if hasattr(A,'fragment'):DN=A.fragment
elif hasattr(A,'experimental_fragment'):DN=A.experimental_fragment
else:
	def DN(func=D,**B):
		if func is not D:return func
		def A(f):return f
		return A
A.markdown('\n<style>\n    /* Force EVERY tab-bar container to wrap onto multiple lines instead of\n       staying on one scrollable line. Multiple selector variants are used\n       (data-baseweb, role, and Streamlit\'s own class) because Streamlit\'s\n       internal DOM/class names have changed across versions. */\n    div[data-testid="stTabs"],\n    div[data-testid="stTabs"] > div,\n    .stTabs,\n    .stTabs > div {\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        max-width: 100% !important;\n    }\n\n    div[data-baseweb="tab-list"],\n    div[role="tablist"] {\n        display: flex !important;\n        flex-wrap: wrap !important;\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        white-space: normal !important;\n        row-gap: 4px !important;\n        column-gap: 6px !important;\n        height: auto !important;\n        max-width: 100% !important;\n        width: 100% !important;\n        scrollbar-width: none !important;\n    }\n    div[data-baseweb="tab-list"]::-webkit-scrollbar {\n        display: none !important;\n    }\n\n    /* Each tab button: allow shrinking/wrapping instead of forcing one line */\n    button[data-baseweb="tab"],\n    div[role="tablist"] > button,\n    div[role="tablist"] [role="tab"] {\n        flex: 0 0 auto !important;\n        white-space: normal !important;\n        margin-top: 1px !important;\n        margin-bottom: 1px !important;\n        padding-top: 6px !important;\n        padding-bottom: 6px !important;\n        height: auto !important;\n    }\n\n    /* Hide the "‹ ›" scroll-arrow buttons Streamlit shows when a tab bar overflows */\n    button[data-testid="stTabsScrollButton"],\n    div[data-baseweb="tab-list"] ~ button,\n    div[data-baseweb="tab-list"] + button,\n    button[kind="tabScroll"],\n    button[aria-label*="scroll" i] {\n        display: none !important;\n    }\n\n    div[data-baseweb="tab-highlight"] {\n        display: none !important;\n    }\n    div[data-baseweb="tab"][aria-selected="true"],\n    [role="tab"][aria-selected="true"] {\n        background-color: rgba(31, 119, 180, 0.1) !important;\n        border-radius: 5px !important;\n        border-bottom: 2px solid #1f77b4 !important;\n    }\n</style>\n',unsafe_allow_html=B)
Ch=J
BR=J
if JE in A.secrets:Gv.configure(api_key=A.secrets[JE]);Ch=B
if JF in A.secrets:
	try:from groq import Groq as L6;L7=L6(api_key=A.secrets[JF]);BR=B
	except ImportError:BR=J
Eb=Ch or BR
def Ec(prompt,model_choice):
	A=prompt
	if model_choice==Fv and BR:B=L7.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{'role':'user','content':A}],max_tokens=2048);return B.choices[0].message.content
	elif Ch:C=Gv.GenerativeModel('gemini-2.5-flash');return C.generate_content(A).text
	else:raise RuntimeError('No AI model is configured. Add GEMINI_API_KEY or GROQ_API_KEY to secrets.')
def Ed(key_suffix=C):
	D='🧠 Gemini';C,E=[],0
	if BR:C.append(Fv)
	if Ch:C.append(D)
	if not C:C=[Fv,D]
	return A.radio('🤖 AI Model:',C,index=0,horizontal=B,key=f"ai_model_sel_{key_suffix}")
L8=['Based on the current data provided, give me a quick summary of the technical performance and trend for {sym}. Also give me all other details and calculate if this company is profitable or not.','Analyze the 52-week high and low data for {sym}. Is the stock closer to its peak or bottom? What does this imply for entry or exit timing? Identify the ideal buy zone.','Examine the 50 DMA, 100 DMA, and 200 DMA data for {sym}. Is the stock in a bullish crossover, bearish zone, or consolidation phase? Explain the trend strength and momentum.','Using the volume data for {sym}, identify if there is unusual volume activity. Does the current volume indicate institutional buying, selling, or accumulation? What does it signal?','Evaluate the full fundamentals of {sym} — EPS, RONW%, D/E ratio, Net Profit (Cr.), Book Value, and Market Cap. Is this company financially healthy and worth long-term investment?','What is the risk profile of {sym} based on its Pledged %, Promoters Holding %, Institutional Holding %, and Debt-to-Equity ratio? Should a retail investor be cautious right now?',"Compare {sym}'s current CMP vs its 200 DMA. Is the stock overbought, oversold, or fairly valued based on the Difference from 200 DMA metric? What is the ideal risk-reward entry zone?",'Give a complete Buy / Hold / Sell recommendation for {sym} using all available technical and fundamental data. Include specific price targets, support levels, and a stop-loss level.','Based on the CAR Rating and Output signal for {sym}, what is the system suggesting? Does the historical price action and current data support this signal? How reliable is it?',"Summarize {sym}'s sector positioning, market cap, enterprise value, book value, and promoter holding. How does this stock compare to typical benchmarks in its sector in the Indian market?"]
L9="Strategy 1 — Volume Breakout with Dynamic Stop Loss\n  Rule 1: Enter long when today's volume > 2× the 20-day average volume AND price closes above the prior day's high; set stop loss at 1.5× ATR below entry price.\n  Rule 2: Add a false breakout filter — price must hold above the breakout level for 2 consecutive candles before confirming entry; trail stop at the lowest low of the last 3 bars.\n  Rule 3: Set profit target at 2:1 risk-reward ratio; plot a volume histogram overlay to identify surge bars visually; include an alert condition for live breakout detection.\n\nStrategy 2 — Moving Average Crossover (50/100/200 DMA)\n  Rule 4: Buy when 50 DMA crosses above 100 DMA with price trading above the 200 DMA; exit when 50 DMA crosses back below 100 DMA; use 200 DMA as the hard stop-loss floor.\n  Rule 5: Add RSI confirmation — only enter when RSI is between 50–70 at the crossover candle; plot all three DMAs on the chart with distinct colours for visual clarity.\n  Rule 6: Allow a re-entry if 50 DMA pulls back to 100 DMA without breaking below 200 DMA; set stop loss 2% below the 50 DMA value at the time of entry.\n\nStrategy 3 — Trend Following with Trailing Stop\n  Rule 7: Enter long when price breaks a 20-day high with above-average volume and ADX > 25; apply a Chandelier Exit trailing stop set at 3× ATR from the highest close after entry.\n  Rule 8: Use 200 DMA direction as the trend filter — only take long trades when price is above 200 DMA; tighten trailing stop to 2× ATR once profit exceeds 10% from entry.\n  Rule 9: Add a re-entry condition: if stopped out but price remains above 200 DMA, re-enter on the next pullback to the 50 DMA; limit to a maximum of 2 re-entries per trend leg.\n\nStrategy 4 — Mean Reversion from 52W High/Low\n  Rule 10: Buy when price is within 15% of the 52-week low AND RSI < 35; set profit target at the 52-week midpoint; place hard stop loss 5% below the 52-week low level.\n  Rule 11: Exit/short signal when price is within 5% of the 52-week high with RSI > 70; use Bollinger Band upper band touch as secondary confirmation; target the middle Bollinger Band as exit.\n  Rule 12: Apply a volume reversal filter — only enter when the reversal candle's volume is ≥ 1.5× the 20-day average; plot the 52-week high and low as horizontal reference lines on the chart."
LA='\n### 💡 Core Rules\n- **Sheet Convention:** Always use **NSE Code** instead of *Symbol* in the Google Sheet — this keeps NSE chart links working correctly.\n- **No Compromise:** Follow the Rules. Never compromise on Rules — Rules are better than any single Buy/Sell decision.\n- **Timing Edge:** Take advantage of time — buy when a stock is at its lower end (near 52W Low) and sell at a higher price when momentum kicks in (e.g. an Upper Circuit move).\n\n---\n\n### 🟢 Rule 1 — Near 52 Week High\nCMP / Close Price is highlighted **Green** when it is near the 52-Week High (within ~8%).\n\n### 🟠 Rule 2 — Near 52 Week Low (Buy Zone)\nCMP / Close Price is highlighted **Orange** when it is near the 52-Week Low (within ~8%) — **this is the type of stock to look at buying.**\n\n**52W Low / High Date column — color meaning:**\n| Signal | Meaning |\n|---|---|\n| 🟢 Green in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 18 days** |\n| 🟢 Green in *52 Week High Date* | Stock touched its 52-Week High within the **last 18 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 30 days** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High within the **last 30 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low **about 1 year ago** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High **about 1 year ago** |\n\n### 🔵 Rule 3 — Diff @ 200 DMA Strategy\nOnly buy **52-Week Low** stocks, ranked by the **Difference from 200 DMA** column on the **Diff @ 200 DMA** tab — biggest fall first.\n\n**Path:**\n1. Open the **Diff @ 200 DMA** tab (Main sheet).\n2. Refer to the **Difference from 200 DMA** column.\n3. Sort results **−40% → −30% → −20% → −10%** (most negative first).\n\n**Mind Map:**\n```\nRule 3 → Buy Only 52-Week Low Stocks\n│\n├── Main Sheet → Open Tab "Diff @ 200 DMA"\n├── Check Column → "Difference from 200 DMA"\n├── Sort Logic → Biggest Fall First (-40% → -30% → -20% → -10%)\n├── Meaning → Stock is trading below its 200 DMA\n├── Priority → More negative % = higher priority\n├── Selection Criteria\n│     ├── Only 52-Week Low stocks\n│     ├── Negative Difference from 200 DMA\n│     └── Deep-discount stocks preferred\n└── Final Action → Analyze & buy quality stocks\n```\n\n---\n\n### 🔗 Useful NSE Reference Links\n- **All Reports (Bhavcopy / Market Activity):** Bhavcopy (PR)(zip), Market Activity Report (csv), Full Bhavcopy & security delivery data, MCAP, PD, PR, SME → https://www.nseindia.com/all-reports/\n- **Securities Available for Trading** (ETF, Close-Ended MF Schemes, SME) → https://www.nseindia.com/static/market-data/securities-available-for-trading\n- **52-Week Low — Equity Market** → https://www.nseindia.com/market-data/52-week-low-equity-market#capital_market_link\n\n---\n\n### 🛑 Risk Management — No Compromise\n- **Stop Loss (Max 1–2%), no compromise.** બીજો chance મળશે કમાવાનો — પૈસા 10% ઓછા થયા તો 15% કમાવા પડશે.\n- **Risk-Reward Ratio:** max 5 trades, max 10% loss — never lose all your money in a single trade.\n- **Target / Profit Booking:** Max 10–20%.\n- Don\'t trade emotionally — the share market is a mind game.\n- Know everything related to a share before moving ahead.\n- Stay calm, serious, and stick to the decision you\'ve made.\n- **Clear Vision, no compromise:** Focus → Stop Loss → Risk-Reward Ratio → Target/Profit → 52-Week Low Buy.\n- **Priority order:** IPO → F&O → 52-Week Low Shares.\n'
LB={BH:['50 DMA','100 DMA','200 DMA','NSE 1','Trading View 1','History Data 1','Screener 1','Zerodha 1','Chartlink 1','Market smith india 1','Official NSE URL 1'],BI:[],CO:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
LC={BH:['E','F','G','AA','AB','AC','AD','AE','AF','AG','AH'],BI:[],CO:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
def Gw(letter):
	A=letter;A=G(A).strip().upper()
	if not A or not A.isalpha():return-1
	B=0
	for C in A:B=B*26+(ord(C)-ord('A')+1)
	return B-1
def LD(sheet_name,ordered_columns):
	C=sheet_name;A=ordered_columns;A=AO(A);B=set()
	for D in LB.get(C,[]):
		if D in A:B.add(D)
	for F in LC.get(C,[]):
		E=Gw(F)
		if 0<=E<S(A):B.add(A[E])
	return B
LE={BH:D,BI:D,CO:D,CP:D,CQ:D,CR:D,CS:D,CT:D}
LF={BH:[Ao,s,'Close Price',AP,JG,Ap,Aq,JH,'Differance from 200 DMA','Cumulative Average Rule (CAR) Rating'],BI:[],CO:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
LG={BH:['B','C','D','L'],BI:[],CO:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
def LH(sheet_name,ordered_columns):
	D=sheet_name;A=ordered_columns;A=AO(A);B=[]
	for G in LG.get(D,[]):
		E=Gw(G)
		if 0<=E<S(A):
			F=A[E]
			if F not in B:B.append(F)
	for C in LF.get(D,[]):
		if C in A and C not in B:B.append(C)
	return B
import streamlit as A
LI='\n<style>\n    #MainMenu {visibility: show;}\n    header {visibility: show;}\n    [data-testid="stToolbar"] {visibility: show;}\n    footer {visibility: show;}\n</style>\n'
A.markdown(LI,unsafe_allow_html=B)
import streamlit as A
LJ='\n<style>\n    [data-testid="stToolbar"] {\n        right: 2rem;\n    }\n    [data-testid="stToolbar"]::before {\n        content: "";\n    }\n    button[kind="header"] {display: none;}\n</style>\n'
A.markdown(LJ,unsafe_allow_html=B)
LK='romo'
if'logged_in'not in A.session_state:A.session_state.logged_in=J
if'watchlist'not in A.session_state:A.session_state.watchlist={}
if'ai_history'not in A.session_state:A.session_state.ai_history=[]
if'grid_reset_token'not in A.session_state:A.session_state.grid_reset_token=0
if not A.session_state.logged_in:
	A.markdown("<p style='text-align: center; margin-top: 100px; color: Green; font-size: 18px;'>NF-750-Delivery % (+V) Dashboard</p>",unsafe_allow_html=B);A.markdown("<h1 style='text-align: center; margin-top: 0px; font-size: 20px;'>🔐 Admin Login</h1>",unsafe_allow_html=B);Ot,LL,Ou=A.columns([1,1,1])
	with LL:
		with A.form('login_form'):
			LM=A.text_input('Enter Password',type='password');LN=A.form_submit_button('Login',use_container_width=B)
			if LN:
				if LM==LK:A.session_state.logged_in=B;A.rerun()
				else:import random;LO=['Password इल्ले! 😅 इल्ले!, खम्मा घणी भाईसा, सॉरी। तुमसे सब कुछ हो पाएगा! यहां बहुत 🤪 दिमाग मत लगाओ, इस वेबसाइट को नहीं, 😂 इस गलत पासवर्ड को छोड़ दो!','❌ Password इल्ले भाईसा! 😅 इल्ले! खम्मा घणी, सॉरी। तुम बाहुबली हो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। अपनी सुंदर वेबसाइट को नहीं, 😂 इस सड़े हुए गलत पासवर्ड को छोड़ दो!','❌ खम्मा घणी भाईसा, Password इल्ले! 😅 sorry! तुम तो मंगल ग्रह पर पानी खोज सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस सीधे-सादे वेबसाइट को नहीं, 😂 इस जाली पासवर्ड को छोड़ दो!','❌ Password इल्ले! 😅 इल्ले! खम्मा घणी भाईसा, सॉरी। लोड मत लो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। दुनिया छोड़ दो, मोक्ष पकड़ लो, पर पहले 😂 इस गलत पासवर्ड को छोड़ दो!','❌ अरे भाईसा! Password इल्ले! 😅 खम्मा घणी, सॉरी। तुम चाहो तो सिस्टम हिला सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस निर्दोष वेबसाइट को नहीं, 😂 इस भूतिया गलत पासवर्ड को छोड़ दो!'];A.error(random.choice(LO))
	LP=m.now().strftime(CU);A.markdown(f"<p style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>Data refreshed: {LP}</p>",unsafe_allow_html=B);A.stop()
A.markdown('\n<style>\n    /* Reduce ALL headings to 90% smaller size */\n    h1, h2, h3, h4, h5, h6, .stSubheader, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {\n        font-size: 0.85rem !important;\n        font-weight: bold !important;\n        margin-top: 0.5rem !important;\n        margin-bottom: 0.5rem !important;\n    }\n</style>\n',unsafe_allow_html=B)
import yfinance as Gx,streamlit as A
from datetime import datetime as m
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📊 NF-750-Delivery % (+V)</p>",unsafe_allow_html=B)
A.caption(f"Data refreshed: {m.now().strftime(CU)}")
@A.cache_data(ttl=60)
def LQ():
	A='UNSUPPORTED';H={'NIFTY 50':'^NSEI','NIFTY NEXT 50':'^NN50','NIFTY MIDCAP 50':'^NSEMDCP50','NIFTY MIDCAP 100':'^CRSLMID','NIFTY MIDCAP 150':A,'NIFTY SMLCAP 50':A,'NIFTY SMLCAP 100':A,'NIFTY SMLCAP 250':A,'NIFTY MIDSML 400':A,'NIFTY 100':'^CNX100','NIFTY 200':'^CNX200','NIFTY500 MULTI...':A,'NIFTY LARGEMID...':A,'NIFTY MID SELE...':A,'NIFTY TOTAL MK...':A,'NIFTY MICROCAP...':A,'NIFTY 500':'^CRSLDX','NIFTY FPI 150':A,'NIFTY500 LMS E...':A,'NIFTY MIDSMALL...':A,'NIFTY SMALLCAP...':A};B={}
	for(C,E)in H.items():
		if E==A:B[C]={B4:Dz,A2:i};continue
		try:
			I=Gx.Ticker(E);D=I.history(period='5d')
			if not D.empty and S(D)>=2:F=M(D[BJ].iloc[-1]);G=M(D[BJ].iloc[-2]);J=(F-G)/G*100;B[C]={B4:f"{F:,.2f}",A2:J}
			else:B[C]={B4:Fw,A2:i}
		except g:B[C]={B4:Fx,A2:i}
	return B
LR=LQ()
Av=JI
Gy=0
for(B_,AV)in LR.items():
	if AV[B4]in[Dz,Fw,Fx]:continue
	Gy+=1;Ee=D2 if AV[A2]>=0 else Fy;Ef='+'if AV[A2]>=0 else C;LS='https://www.nseindia.com/market-data/live-market-indices';Av+=f"<a href='{LS}' target='_blank' style='text-decoration:none;'>";Av+=f"<div style='background-color: {Ee}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";Av+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{B_}</div>";Av+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";Av+=f"<span style='font-size: 15px; font-weight: 700;'>{AV[B4]}</span>";Av+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{Ef}{AV[A2]:.2f}%</span>";Av+=f"</div></div></a>"
Av+=D3
with A.expander('📈 Click to view Live Market Indices',expanded=J):
	if Gy==0:A.info('Market data is currently unavailable. Please check back later.')
	else:A.markdown(Av,unsafe_allow_html=B)
A.write(c)
def Gz(color_dict):
	A=color_dict
	if not A:return D4
	B,C,D=U(A.get('red',0)*255),U(A.get('green',0)*255),U(A.get('blue',0)*255);return f"#{B:02x}{C:02x}{D:02x}"
@A.cache_data(ttl=300,show_spinner=J)
def LT(nse_symbol,period='1y'):
	try:
		C=G(nse_symbol).strip().upper()
		if not C:return H.DataFrame()
		E=C if C.endswith('.NS')else f"{C}.NS";A=Gx.download(E,period=period,interval='1d',progress=J,auto_adjust=B)
		if A is D or A.empty:return H.DataFrame()
		if B3(A.columns,H.MultiIndex):A.columns=A.columns.get_level_values(0)
		A.index=H.to_datetime(A.index);return A
	except g:return H.DataFrame()
@A.cache_data(ttl=300)
def DO(sheet_name):
	M='sheets'
	try:
		if D_ not in A.secrets:A.error("Missing 'gcp_service_account' in secrets.");return H.DataFrame()
		D=A.secrets[D_]
		if B3(D,G):D=EY.loads(D)
		Y=[JJ,JK];N=Gu.from_service_account_info(D,scopes=Y);j=EX.authorize(N);Z=JL;a=urllib.parse.quote(sheet_name);b=L3(N);c=f"https://sheets.googleapis.com/v4/spreadsheets/{Z}?includeGridData=true&ranges={a}";d=b.get(c);E=d.json()
		if'error'in E:return H.DataFrame()
		if M not in E or not E[M]:return H.DataFrame()
		e=E[M][0]['data'][0];O=e.get('rowData',[])
		if not O:return H.DataFrame()
		J,P,Q=[],[],[]
		for f in O:
			h=f.get('values',[]);R,T,U=[],[],[]
			for V in h:R.append(V.get('formattedValue',C));W=V.get('effectiveFormat',{});T.append(Gz(W.get('backgroundColor',{})));U.append(Gz(W.get('textFormat',{}).get('foregroundColor',{})))
			J.append(R);P.append(T);Q.append(U)
		i=J[0];K=[];F={}
		for B in i:
			B=G(B).strip()
			if B==C:B='empty_column'
			if B in F:F[B]+=1;B=f"{B}_{F[B]}"
			else:F[B]=0
			K.append(B)
		L=H.DataFrame(J[1:],columns=K)
		for(I,X)in Dx(K):L[f"_bg_{X}"]=[A[I]if I<S(A)else D4 for A in P[1:]];L[f"_txt_{X}"]=[A[I]if I<S(A)else'#000000'for A in Q[1:]]
		return L
	except g as k:return H.DataFrame()
def LU(df,symbol_col):
	K=symbol_col;H='1';F='🔗 Link';I=df.copy();I[o]=I[K]
	for(L,M)in I.iterrows():
		A=G(M[o]).strip()
		if not A or A==A8:continue
		for J in I.columns:
			if J.startswith(Ab)or J.startswith(Ac)or J==o:continue
			B=J.lower();C,E=D,F
			if JM in B:C,E=f"https://www.tradingview.com/symbols/{A}/",f"Tre {A}"if not B.endswith(H)else F
			elif JN in B:C,E=f"https://www.equitypandit.com/historical-data/{A}",f"History {A}"if not B.endswith(H)else F
			elif JO in B:C,E=f"https://www.screener.in/company/{A}",f"Scr {A}"if not B.endswith(H)else F
			elif JP in B:C,E=f"https://zerodha.com/markets/stocks/NSE/{A}",f"🪁 {A}"if not B.endswith(H)else F
			elif JQ in B:C,E=f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={A}",f"CL {A}"if not B.endswith(H)else F
			elif JR in B:C,E=f"https://marketsmithindia.com/mstool/eval/{A}/evaluation.jsp",f"ms {A}"if not B.endswith(H)else F
			elif JS in B:C,E=f"https://www.nseindia.com/get-quotes/equity?symbol={A}",f"nse📰 {A}"if not B.endswith(H)else F
			elif'nse'in B or J==K:C,E=f"https://charting.nseindia.com/?symbol={A}-EQ",A if not B.endswith(H)else F
			if C:I.at[L,J]=f'<a href="{C}" target="_blank" style="text-decoration:none; color:#000000;">{E}</a>'
	return I
def DP(df,col_name,st_container,display_label=D):
	J=display_label;D=col_name
	if D in df.columns:
		A=df[D].astype(G).str.replace(BK,C,regex=B);A=H.to_numeric(A,errors=AQ).replace([AA.inf,-AA.inf],AA.nan);E=A.dropna()
		if not E.empty:
			F,I=b(M(E.min()),2),b(M(E.max()),2)
			if F<I:L=J if J else f"{D} Range:";K=st_container.slider(L,min_value=F,max_value=I,value=(F,I),key=f"filter_num_{D}");return df[(A>=K[0])&(A<=K[1])]
	return df
def G_(df,col_name,st_container):
	Q='Past 1 Year';P='Past 6 Months';O='Past 2 Months';N='Past 1 Month';M='Past 30 Days';L='Past 25 Days';K='Past 20 Days';J='Past 15 Days';I='Past 10 Days';G='Past 5 Days';F='All Time';E=col_name
	if E in df.columns:
		R=[F,G,I,J,K,L,M,N,O,P,Q];A=st_container.selectbox(f"{E}:",R,key=f"filter_date_{E}")
		if A!=F:
			S=H.to_datetime(df[E],errors=AQ,dayfirst=B);C=H.Timestamp.now()
			if A==G:D=C-H.Timedelta(days=5)
			elif A==I:D=C-H.Timedelta(days=10)
			elif A==J:D=C-H.Timedelta(days=15)
			elif A==K:D=C-H.Timedelta(days=20)
			elif A==L:D=C-H.Timedelta(days=25)
			elif A==M:D=C-H.Timedelta(days=30)
			elif A==N:D=C-H.DateOffset(months=1)
			elif A==O:D=C-H.DateOffset(months=2)
			elif A==P:D=C-H.DateOffset(months=6)
			elif A==Q:D=C-H.DateOffset(years=1)
			return df[S>=D]
	return df
def C0(val):
	if H.isna(val):return 0
	A=re.sub(E0,C,G(val));return S(A)
def H0(df):
	A=df.copy();D=[A for A in A.columns if A.startswith(Ab)or A.startswith(Ac)or A==o];A=A.drop(columns=D,errors='ignore')
	for B in A.select_dtypes(include=['object']).columns:A[B]=A[B].apply(lambda x:re.sub(E0,C,G(x))if H.notnull(x)else x)
	return A
import streamlit.components.v1 as Q
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>🌍 National Exchange Scanner (All NSE/BSE Stocks)</p>",unsafe_allow_html=B)
A.caption('Live market data covering 2,000+ equities. Powered by TradingView.')
with A.expander('🏆 Click to view Full-Market India Rankings',expanded=J):
	LV,LW,LX,LY,LZ=A.tabs(['🚀 Gainers & Losers','📦 Volume & Active','⭐ 52W High / Low','🔄 52W Reversals','📊 Top 100 Traded'])
	def Aw(screen_type):return f'''
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
          {{
          "width": "100%",
          "height": "500",
          "defaultColumn": "overview",
          "defaultScreen": "{screen_type}",
          "market": "india",
          "showToolbar": true,
          "colorTheme": "light",
          "locale": "en"
        }}
          </script>
        </div>
        '''
	with LV:
		Ax,Ay=A.columns(2)
		with Ax:A.markdown("<p style='font-size:14px; font-weight:bold;'>🚀 Top Gainers</p>",unsafe_allow_html=B);Q.html(Aw('top_gainers'),height=520)
		with Ay:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔻 Top Losers</p>",unsafe_allow_html=B);Q.html(Aw('top_losers'),height=520)
	with LW:
		Ax,Ay=A.columns(2)
		with Ax:A.markdown("<p style='font-size:14px; font-weight:bold;'>📦 Volume Leaders</p>",unsafe_allow_html=B);Q.html(Aw('volume_leaders'),height=520)
		with Ay:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔥 Most Active (Volume & Value)</p>",unsafe_allow_html=B);Q.html(Aw('most_active'),height=520)
	with LX:
		Ax,Ay=A.columns(2)
		with Ax:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Highs</p>",unsafe_allow_html=B);Q.html(Aw('new_52wk_high'),height=520)
		with Ay:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Lows</p>",unsafe_allow_html=B);Q.html(Aw('new_52wk_low'),height=520)
	with LY:
		Ax,Ay=A.columns(2)
		with Ax:A.markdown("<p style='font-size:14px; font-weight:bold;'>📈 Outperforming 52W High (Reversal Up)</p>",unsafe_allow_html=B);Q.html(Aw('outperforming_52wk_high'),height=520)
		with Ay:A.markdown("<p style='font-size:14px; font-weight:bold;'>📉 Underperforming 52W Low (Reversal Down)</p>",unsafe_allow_html=B);Q.html(Aw('underperforming_52wk_low'),height=520)
	with LZ:A.markdown("<p style='font-size:14px; font-weight:bold;'>📊 Top 100+ Stocks Traded (Full India Screener)</p>",unsafe_allow_html=B);Q.html(Aw('general'),height=520)
A.write(c)
@A.cache_data(ttl=300)
def La():
	E=DO(BH);A={}
	if E.empty:return A
	B=[A for A in E.columns if not A.startswith(Ab)and not A.startswith(Ac)];J=R((A for A in B if A.lower()in[D5,Ad,E1,E2,D6,E3]),D);K=R((A for A in B if A3 in A.lower()),D);F=R((A for A in B if CV in A.lower()or A2 in A.lower()),D);F=R((A for A in B if t in A or'pct'in A.lower()or JT in A.lower()),D)
	if not J or not K:return A
	for(S,H)in E.iterrows():
		I=G(H.get(J,C)).strip()
		if not I or I==A8:continue
		O=G(H.get(K,C)).replace(AE,C).strip();P=G(H.get(F,'0')).replace(t,C).replace(AE,C).strip()if F else'0'
		try:Q=M(O);L=f"{Q:,.2f}"
		except AZ:L=Dz
		try:N=M(P)
		except AZ:N=i
		A[I]={B4:L,A2:N}
	return A
Lb=La()
Az=JI
H1=0
for(B_,AV)in Lb.items():
	if AV[B4]in[Dz,Fw,Fx]:continue
	H1+=1;Ee=D2 if AV[A2]>=0 else Fy;Ef='+'if AV[A2]>=0 else C;Lc=f"https://www.nseindia.com/get-quotes/equity?symbol={B_}";Az+=f"<a href='{Lc}' target='_blank' style='text-decoration:none;'>";Az+=f"<div style='background-color: {Ee}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";Az+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{B_}</div>";Az+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";Az+=f"<span style='font-size: 15px; font-weight: 700;'>{AV[B4]}</span>";Az+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{Ef}{AV[A2]:.2f}%</span>";Az+=f"</div></div></a>"
Az+=D3
with A.expander('📈 Click to view Top 250 Stocks Matrix',expanded=J):
	if H1==0:A.info("Stock matrix data is currently unavailable. Please check the 'NSE Price Data' sheet.")
	else:A.markdown(Az,unsafe_allow_html=B)
A.write(c)
@A.cache_data(ttl=300)
def Ld():
	P='[a-zA-Z%, ]';E=DO(BH)
	if E.empty:return H.DataFrame()
	F=[A for A in E.columns if not A.startswith(Ab)and not A.startswith(Ac)];J=R((A for A in F if A.lower()in[D5,Ad,E1,E2,D6,E3]),D);K=R((A for A in F if A3 in A.lower()),D);I=R((A for A in F if t in A or'pct'in A.lower()or JT in A.lower()),D);I=R((A for A in F if CV in A.lower()or A2 in A.lower()),D);L=R((A for A in F if BL in A.lower()),D);M=R((A for A in F if E4 in A.lower()and'face'not in A.lower()and'enterprise'not in A.lower()),D);N=R((A for A in F if Bl in A.lower()),D)
	if not J:return H.DataFrame()
	A=H.DataFrame();A[j]=E[J].astype(G).str.strip();A[AP]=H.to_numeric(E[K].astype(G).str.replace(BK,C,regex=B),errors=AQ)if K else i;A[E5]=H.to_numeric(E[I].astype(G).str.replace(BK,C,regex=B),errors=AQ)if I else i;A[s]=H.to_numeric(E[L].astype(G).str.replace(BK,C,regex=B),errors=AQ)if L else i;O=A[AP]*A[s]
	if M:A[CW]=H.to_numeric(E[M].astype(G).str.replace(P,C,regex=B),errors=AQ)
	else:A[CW]=O
	if N:A[D7]=H.to_numeric(E[N].astype(G).str.replace(P,C,regex=B),errors=AQ)
	else:A[D7]=O
	A=A.dropna(subset=[j,AP]).reset_index(drop=B);A=A[(A[j]!=A8)&(A[j]!=C)];return A
def B9(dataframe,metric_label=A2):
	J=dataframe;G=metric_label;A="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; font-family: system-ui, -apple-system, sans-serif;'>"
	if J.empty:return"<p style='color: gray; font-size: 14px;'>No data available for this ranking.</p>"
	for(R,B)in J.iterrows():
		K=B[j];L=B[AP];H=B[E5];M=D2 if H>=0 else Fy;N='+'if H>=0 else C
		if G==BL:D=B.get(s,0);F=f"Vol: {D/1000000:.1f}M"if D>=1000000 else f"Vol: {D:,.0f}"
		elif G==E4:E=B.get(CW,0);F=f"Val: ₹{E/10000000:,.1f}Cr"if E>=10000000 else f"Val: ₹{E:,.0f}"
		elif G==Bl:I=B.get(D7,0);F=f"T.O: ₹{I/10000000:,.1f}Cr"if I>=10000000 else f"T.O: ₹{I:,.0f}"
		elif G==JU:D=B.get(s,0);E=B.get(CW,0);O=f"{D/1000000:.1f}M"if D>=1000000 else f"{D/1000:.1f}k";P=f"₹{E/10000000:,.1f}Cr"if E>=10000000 else f"₹{E:,.0f}";F=f"📦 {O} | 💰 {P}"
		else:F=f"{N}{H:.2f}%"
		Q=f"https://www.nseindia.com/get-quotes/equity?symbol={K}";A+=f"<a href='{Q}' target='_blank' style='text-decoration:none;'>";A+=f"<div style='background-color: {M}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";A+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{K}</div>";A+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";A+=f"<span style='font-size: 15px; font-weight: 700;'>{L:,.2f}</span>";A+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px; white-space: nowrap;'>{F}</span>";A+=f"</div></div></a>"
	A+=D3;return A
Ai=Ld()
with A.expander('🏆 Click to view Advanced Ranking Dashboards (NSE Price Data)',expanded=J):
	if Ai.empty:A.info("Ranking data is currently unavailable. Please check the 'NSE Price Data' sheet.")
	else:
		Le=Ai.nlargest(20,E5);Lf=Ai.nsmallest(20,E5);Lg=Ai.nlargest(20,s);Lh=Ai[Ai[s]>0].nsmallest(20,s);Li=Ai.nlargest(20,s);Lj=Ai.nlargest(20,CW);Lk=Ai.nlargest(20,D7);Ll=Ai.nlargest(20,CW);Lm,Ln,Lo,Lp,Lq,Lr=A.tabs(['📈 Gainers/Losers','📦 Volume Leaders','🔥 Active (Vol & Val)','💰 Top by Value','💎 Top by Turnover','💰 Most Active'])
		with Lm:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🚀 Top 20 Gainers</p>",unsafe_allow_html=B);A.markdown(B9(Le,A2),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔻 Top 20 Losers</p>",unsafe_allow_html=B);A.markdown(B9(Lf,A2),unsafe_allow_html=B)
		with Ln:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>📦 Top 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B9(Lg,BL),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💤 Bottom 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B9(Lh,BL),unsafe_allow_html=B)
		with Lo:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔥 Most Active Stocks (Volume & Traded Value)</p>",unsafe_allow_html=B);A.markdown(B9(Li,JU),unsafe_allow_html=B)
		with Lp:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active by Traded Value</p>",unsafe_allow_html=B);A.markdown(B9(Lj,E4),unsafe_allow_html=B)
		with Lq:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💎 Highest Market Turnover</p>",unsafe_allow_html=B);A.markdown(B9(Lk,Bl),unsafe_allow_html=B)
		with Lr:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active (Highest Traded Value)</p>",unsafe_allow_html=B);A.markdown(B9(Ll,E4),unsafe_allow_html=B)
A.write(c)
def DQ(row,actual_cols):
	B=0;A=[]
	def E(col_keywords,negate=J):
		for E in col_keywords:
			A=R((A for A in actual_cols if E.lower()in A.lower()),D)
			if A and A in row:
				try:B=M(G(row[A]).replace(t,C).replace(AE,C).strip());return-B if negate else B
				except:pass
	O=E([A3]);S=E([JV,CX,'52wlow'])
	if O and S and S>0:
		K=(O-S)/S*100
		if 8<=K<=15:B+=30;A.append(f"✅ CMP +{K:.1f}% from 52W Low (sweet zone)")
		elif K<8:B+=15;A.append(f"⚠️ CMP +{K:.1f}% from 52W Low (still bottoming)")
		elif K<=25:B+=10;A.append(f"🟡 CMP +{K:.1f}% from 52W Low (extended)")
		else:A.append(f"❌ CMP +{K:.1f}% from 52W Low (too far)")
	P=E([Fz])
	if O and P and P>0:
		if O>P:B+=15;A.append('✅ CMP above 200 DMA (uptrend confirmed)')
		else:
			V=(O-P)/P*100
			if V>-10:B+=7;A.append(f"🟡 CMP {V:.1f}% below 200 DMA (near support)")
			else:A.append(f"❌ CMP {V:.1f}% below 200 DMA (downtrend)")
	L=E([Bl,BL])
	if L and L>0:
		if L>=10000000:B+=10;A.append(f"✅ High volume: {L:,.0f}")
		elif L>=1000000:B+=6;A.append(f"🟡 Moderate volume: {L:,.0f}")
		else:B+=2;A.append(f"⚠️ Low volume: {L:,.0f}")
	F=E([JW,'debt','d/e'])
	if F is not D:
		if F<=.1:B+=10;A.append(f"✅ Debt-Free / Zero Debt (D/E={F:.2f})")
		elif F<=.5:B+=7;A.append(f"✅ Very Low Debt (D/E={F:.2f})")
		elif F<=Ar:B+=4;A.append(f"🟡 Manageable Debt (D/E={F:.2f})")
		else:A.append(f"❌ High Debt (D/E={F:.2f})")
	T=E([E6])
	if T is not D:
		if T>0:B+=10;A.append(f"✅ Profitable: Net Profit ₹{T:.1f} Cr")
		else:A.append(f"❌ Loss Making: Net Profit ₹{T:.1f} Cr")
	H=E(['ronw'])
	if H is not D:
		if H>=15:B+=10;A.append(f"✅ Strong RONW: {H:.1f}%")
		elif H>=8:B+=6;A.append(f"🟡 Moderate RONW: {H:.1f}%")
		elif H>0:B+=2;A.append(f"⚠️ Low RONW: {H:.1f}%")
		else:A.append(f"❌ Negative RONW: {H:.1f}%")
	N=E([F_,G0])
	if N is not D:
		if N>=50:B+=8;A.append(f"✅ Promoter Holding: {N:.1f}%")
		elif N>=35:B+=5;A.append(f"🟡 Promoter Holding: {N:.1f}%")
		else:A.append(f"⚠️ Low Promoter: {N:.1f}%")
	Q=E([G1,G2])
	if Q is not D:
		if Q==0:B+=7;A.append('✅ Zero Pledged Shares')
		elif Q<=5:B+=4;A.append(f"🟡 Low Pledge: {Q:.1f}%")
		else:A.append(f"❌ High Pledge: {Q:.1f}%")
	I=E([G3,BM])
	if I is not D:
		if I>=70:B+=10;A.append(f"✅ % Delivery: {I:.1f}% (strong institutional buying)")
		elif I>=50:B+=6;A.append(f"🟡 % Delivery: {I:.1f}% (moderate genuine buying)")
		elif I>=30:B+=3;A.append(f"⚠️ % Delivery: {I:.1f}% (mostly intraday)")
		else:A.append(f"❌ % Delivery: {I:.1f}% (speculative / intraday dominated)")
	W=E([E7,'net sale'])
	if W and W>0:A.append(f"📊 Net Sales: ₹{W:.1f} Cr")
	if B>=75:U='🟢 STRONG BUY'
	elif B>=55:U='🟡 WATCHLIST'
	elif B>=35:U='🟠 CAUTION'
	else:U='🔴 AVOID'
	return B,U,A
H2=G4
def H3():
	if D_ not in A.secrets:return
	B=A.secrets[D_]
	if B3(B,G):B=EY.loads(B)
	C=[JJ,JK];D=Gu.from_service_account_info(B,scopes=C);return EX.authorize(D)
Ls=JL
def H4(client):
	try:
		A=client.open_by_key(Ls)
		try:return A.worksheet(H2)
		except EX.WorksheetNotFound:B=A.add_worksheet(title=H2,rows=500,cols=6);B.append_row([j,AP,D8,D9,E8,E9]);return B
	except g:return
def Lt():
	D=H3()
	if not D:return
	E=H4(D)
	if not E:return
	try:
		I=E.get_all_records();F={}
		for B in I:
			H=G(B.get(j,C)).strip()
			if H:F[H]={BN:G(B.get(D8,C)),A3:G(B.get(AP,C)),CY:G(B.get(D9,C)),Bm:G(B.get(E8,C)),DA:G(B.get(E9,C))}
		A.session_state.watchlist=F
	except g:pass
def Eg():
	F=H3()
	if not F:A.warning('⚠️ Google Sheet write failed — check secrets.');return J
	E=H4(F)
	if not E:return J
	try:
		E.clear();E.append_row([j,AP,D8,D9,E8,E9])
		for(G,D)in A.session_state.watchlist.items():E.append_row([G,D.get(A3,C),D.get(BN,C),D.get(CY,C),D.get(Bm,C),D.get(DA,C)])
		return B
	except g as H:A.warning(f"⚠️ Sheet write error: {H}");return J
def Lu(sym,cmp=C,note=C,bf_score=C,bf_grade=C):A.session_state.watchlist[sym]={A3:cmp,BN:note,CY:bf_score,Bm:bf_grade,DA:m.now().strftime('%Y-%m-%d %H:%M')}
def H5(sym):A.session_state.watchlist.pop(sym,D)
if'watchlist_loaded'not in A.session_state:Lt();A.session_state.watchlist_loaded=B
def Lv(row_data,cols):
	N='sl_standard'
	def E(keys):
		for B in keys:
			for A in cols:
				if B in A.lower():
					try:D=G(row_data.get(A,C)).replace(AE,C).replace(t,C).strip();return M(D)
					except(AZ,Ft):pass
	B=E([A3]);I=E(['52w high',DB,'52wk high']);J=E([JV,CX,'52wk low']);K=E([JX,'50dma']);L=E([Fz,'200dma']);A={A3:B,G5:I,G6:J,'dma50':K,'dma200':L}
	if B and I and J:F=(I-J)/52;A[EA]=b(F,2);A['sl_tight']=b(B-Ar*F,2);A[N]=b(B-1.5*F,2);A['sl_wide']=b(B-2.*F,2);O=2.;H=B-A[N];A['target_1r']=b(B+H*Ar,2);A['target_2r']=b(B+H*O,2);A['target_3r']=b(B+H*3.,2);A[DC]=b(K,2)if K else D;A['trail_sl_200dma']=b(L,2)if L else D;A['risk_pct']=b(H/B*100,2)if B else D
	return A
def Eh(history):
	E='AI Analysis';B=history
	if not B:return b''
	F=H.DataFrame(B,columns=[j,'Model','Query','AI Result','Timestamp']);C=io.BytesIO()
	with H.ExcelWriter(C,engine=DD)as D:F.to_excel(D,index=J,sheet_name=E);A=D.sheets[E];A.column_dimensions['A'].width=12;A.column_dimensions['B'].width=14;A.column_dimensions['C'].width=40;A.column_dimensions['D'].width=80;A.column_dimensions['E'].width=20
	return C.getvalue()
if A.sidebar.button('🧹 Clear All Filters',use_container_width=B):
	for Ei in AO(A.session_state.keys()):
		if Ei.startswith('filter_')or Ei in(JY,JZ,Ja,Jb):del A.session_state[Ei]
	A.session_state.grid_reset_token+=1;A.rerun()
A.sidebar.markdown(c)
A.sidebar.header('🔍 Global Search')
H6=A.sidebar.text_input('Search by Symbol, Name, etc...',key=JY)
A.sidebar.markdown(c)
A.sidebar.header('📑 Select a Tab')
Lw=[BH,BI,CO,CP,CQ,CR,CS,CT]
A4=A.sidebar.selectbox('Choose sheet',Lw,key='filter_sheet')
A.markdown(f"<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📄 {A4}</p>",unsafe_allow_html=B)
with A.spinner('Downloading data from Google API...'):Ej=DO(A4)
if not Ej.empty:
	Ek=0;O=[A for A in Ej.columns if not A.startswith(Ab)and not A.startswith(Ac)];Lx=LD(A4,O);El=LE.get(A4)
	if El and El in O:Ek=O.index(El)
	else:
		for(BS,Ly)in Dx(O):
			if Ly.lower()in[D5,Ad,E1,E2,D6,E3]:Ek=BS;break
	A.sidebar.markdown(c);A.sidebar.header('⚙️ Settings');C1=A.sidebar.selectbox('Symbol Column (locked):',O,index=Ek,key='filter_symbol_col',disabled=B,help='Locked for consistency across sheets. To change it, edit LOCKED_SYMBOL_COLUMN near the top of the .py file.');H7=LU(Ej,C1);K=H7.copy()
	if H6:Lz=K[O].astype(G).apply(lambda x:x.str.contains(H6,case=J,na=J)).any(axis=1);K=K[Lz]
	A.sidebar.markdown(c);A.sidebar.header('🎨 Color Filters');Em=A.sidebar.selectbox('Select Column to Filter by Color:',[AR]+O,key='filter_color_col')
	if Em!=AR:
		En=f"_bg_{Em}"
		if En in K.columns:
			L_=K[En].unique();Eo={D4:'⚪ White (Default)',A0:'🟢 Green',AS:'🔴 Red',Jc:'🟡 Yellow','#4285f4':'🔵 Blue',Jd:'🟠 Orange','#b6d7a8':'🟩 Light Green','#f4cccc':'🟥 Light Red','#d9d2e9':'🟪 Light Purple'};Ep=[]
			for M0 in L_:
				Eq=G(M0).lower()
				if Eq in Eo:Ep.append(Eo[Eq])
				else:Ep.append(f"🎨 Custom Hex: {Eq}")
			H8=A.sidebar.multiselect(f"Select Colors in '{Em}':",sorted(Ep),key='filter_color_selections')
			if H8:
				Er=[]
				for Es in H8:
					for(M1,B_)in Eo.items():
						if B_==Es:Er.append(M1)
					if Es.startswith(Je):Er.append(Es.replace(Je,C))
				K=K[K[En].str.lower().isin(Er)]
	A.sidebar.markdown(c);A.sidebar.header('🎯 Categorical Filters');M2=[A for A in O if Aa(B in A.lower()for B in['cumulative average',G7,EB,Jf,Jg,G8,G9,GA,Jh,GB])]
	for DR in M2:
		M3=sorted([A for A in H7[DR].unique()if G(A).strip()!=C]);H9=A.sidebar.multiselect(f"Filter by {DR}:",options=M3,key=f"filter_cat_{DR}")
		if H9:K=K[K[DR].isin(H9)]
	A.sidebar.markdown(c);A.sidebar.header('📈 DMA Trend Filter');Ci=A.sidebar.selectbox('Select DMA Condition:',[Ji,Jj,Jk,Jl,Jm],key='filter_dma_trend')
	if Ci!=Ji:
		HA=R((A for A in O if JX in A.lower()),D);HB=R((A for A in O if'100 dma'in A.lower()),D);HC=R((A for A in O if Fz in A.lower()),D)
		if HA and HC:
			DS=H.to_numeric(K[HA].astype(G).str.replace(BK,C,regex=B),errors=AQ);DT=H.to_numeric(K[HC].astype(G).str.replace(BK,C,regex=B),errors=AQ)
			if Ci==Jl:K=K[DS>DT]
			elif Ci==Jm:K=K[DS<DT]
			elif HB:
				DU=H.to_numeric(K[HB].astype(G).str.replace(BK,C,regex=B),errors=AQ)
				if Ci==Jj:K=K[(DS<DU)&(DU<DT)]
				elif Ci==Jk:K=K[(DS>DU)&(DU>DT)]
	A.sidebar.markdown(c);A.sidebar.header('📊 Numeric Range Filters');Et=R((A for A in O if'diff'in A.lower()and'200'in A.lower()),D)
	if Et:K=DP(K,Et,A.sidebar,'Diff. from 200 DMA Range:')
	Eu=R((A for A in O if CZ in A.lower()and GC in A.lower()and(t in A.lower()or'per'in A.lower())),D)
	if Eu:K=DP(K,Eu,A.sidebar,'From 52W Low Range:')
	Ev=R((A for A in O if CZ in A.lower()and GD in A.lower()and(t in A.lower()or'per'in A.lower())),D)
	if Ev:K=DP(K,Ev,A.sidebar,'From 52W High Range:')
	M4=[s,AP,JG,Jn,Jo,Jp,'Net Profit','EPS',Jq,Jr,'Enterprise Value','RSI','Delivery'];HD={Et,Eu,Ev}
	for Cj in M4:
		Ew=R((A for A in O if Cj.lower()in A.lower()and A not in HD),D)
		if Ew:K=DP(K,Ew,A.sidebar);HD.add(Ew)
	A.sidebar.markdown(c);A.sidebar.header('📅 Date Filters');HE=R((A for A in O if Js in A.lower()),D);HF=R((A for A in O if Jt in A.lower()),D)
	if HE:K=G_(K,HE,A.sidebar)
	if HF:K=G_(K,HF,A.sidebar)
	A.sidebar.markdown(c);A.sidebar.header('📊 My Watchlist')
	if A.session_state.watchlist:
		HG=S(A.session_state.watchlist);A.sidebar.caption(f"🔖 {HG} stock{"s"if HG>1 else C} saved")
		for(DV,Ex)in AO(A.session_state.watchlist.items()):
			M5,M6=A.sidebar.columns([3,1]);M5.markdown(f"**{DV}** {"`"+Ex[A3]+"`"if Ex[A3]else C}<br><small style='color:gray'>{Ex.get(BN,C)[:35]}</small>",unsafe_allow_html=B)
			if M6.button('❌',key=f"wl_rm_{DV}",help=f"Remove {DV}"):H5(DV);Eg();A.rerun()
		A.sidebar.markdown(C);M7=H.DataFrame([{j:B,AP:A[A3],D8:A[BN],D9:A.get(CY,C),E8:A.get(Bm,C),E9:A[DA]}for(B,A)in A.session_state.watchlist.items()]);HH=io.BytesIO()
		with H.ExcelWriter(HH,engine=DD)as M8:M7.to_excel(M8,index=J,sheet_name=G4)
		A.sidebar.download_button('📥 Download Watchlist Excel',data=HH.getvalue(),file_name=f"Watchlist_{m.now().strftime(Bn)}.xlsx",mime=Bo,use_container_width=B)
	else:A.sidebar.info('No stocks in watchlist yet.\nAdd from the workspace panel below.')
	if A.session_state.ai_history:
		A.sidebar.markdown(c);A.sidebar.header('🤖 AI History Export');A.sidebar.caption(f"{S(A.session_state.ai_history)} analyses saved this session");M9=Eh(A.session_state.ai_history);A.sidebar.download_button('📥 Download All AI Results (Excel)',data=M9,file_name=f"AI_Analysis_{m.now().strftime(Ju)}.xlsx",mime=Bo,use_container_width=B)
		if A.sidebar.button('🗑️ Clear AI History',use_container_width=B):A.session_state.ai_history=[];A.rerun()
	k=[]
	if C1 in K.columns:k.append(C1)
	DW=R((A for A in O if BM in A.lower()),D)
	if DW and DW not in k:k.append(DW)
	AW=R((A for A in O if BM in A.lower()),D)
	if AW and AW not in k:k.append(AW)
	Aj=R((A for A in O if s in A.lower()),D)
	if Aj and Aj not in k:k.append(Aj)
	Ck=R((A for A in O if GE in A.lower()or'prev'in A.lower()),D)
	if Ck and Ck not in k:k.append(Ck)
	q=R((A for A in O if A3 in A.lower()),D)
	if q and q not in k:k.append(q)
	A1=R((A for A in O if CV in A.lower()),D)
	if A1 and A1 not in k:k.append(A1)
	AL=R((A for A in O if CZ in A.lower()and GD in A.lower()and As not in A.lower()and t not in A.lower()),D)
	if AL and AL not in k:k.append(AL)
	AM=R((A for A in O if CZ in A.lower()and GC in A.lower()and As not in A.lower()and t not in A.lower()),D)
	if AM and AM not in k:k.append(AM)
	AW=R((A for A in O if BM in A.lower()),D);DW=R((A for A in O if BM in A.lower()),D);Aj=R((A for A in O if BL in A.lower()),D);Ck=R((A for A in O if GE in A.lower()or'prev'in A.lower()),D);q=R((A for A in O if A3 in A.lower()),D);A1=R((A for A in O if CV in A.lower()),D);AL=R((A for A in O if CZ in A.lower()and GD in A.lower()and As not in A.lower()and t not in A.lower()),D);AM=R((A for A in O if CZ in A.lower()and GC in A.lower()and As not in A.lower()and t not in A.lower()),D);BT=R((A for A in O if'rsi'in A.lower()),D);Cl=R((A for A in O if G8 in A.lower()),D);BU=R((A for A in O if G9 in A.lower()),D);DX=R((A for A in O if GA in A.lower()and A!=Cl and'dma'not in A.lower()),D);DY=R((A for A in O if'macd'in A.lower()),D);BV=R((A for A in O if GB in A.lower()),D);BW=R((A for A in O if'diff'in A.lower()and'200'in A.lower()),D);HI=LH(A4,O)
	if HI:
		for r in HI:
			if r not in k:k.append(r)
	else:
		for Cj in(Aj,Ck,q,A1,AL,AM):
			if Cj and Cj not in k:k.append(Cj)
	MA=[A for A in K.columns if A not in k and not A.startswith(Ab)and not A.startswith(Ac)and A!=o];MB=[A for A in K.columns if A.startswith(Ab)or A.startswith(Ac)or A==o];MC=k+MA+MB;K=K[MC];A.markdown(c)
	with A.expander(f"🚀 Executive Dashboard — {A4}",expanded=B):
		A.caption('Live snapshot of the currently filtered stock universe. Adjust sidebar filters to update instantly.')
		def Ak(series):
			A=series
			if A is D:return H.Series(dtype=M)
			return H.to_numeric(A.astype(G).str.replace('[%,₹\\s]',C,regex=B),errors=AQ)
		W=K;MD=S(W);Al=Ak(W[A1])if A1 and A1 in W.columns else H.Series(dtype=M);HJ=Ak(W[Aj])if Aj and Aj in W.columns else H.Series(dtype=M);AX=Ak(W[q])if q and q in W.columns else H.Series(dtype=M);BX=Ak(W[AL])if AL and AL in W.columns else H.Series(dtype=M);A_=Ak(W[AM])if AM and AM in W.columns else H.Series(dtype=M);HK=Ak(W[BT])if BT and BT in W.columns else H.Series(dtype=M);HL=Ak(W[AW])if AW and AW in W.columns else H.Series(dtype=M);Ey=R((A for A in O if GF in A.lower()),D);HM=Ak(W[Ey])if Ey and Ey in W.columns else H.Series(dtype=M);v=Ak(W[BW])if BW and BW in W.columns else H.Series(dtype=M);Ez=R((A for A in O if Bl in A.lower()),D);HN=Ak(W[Ez])if Ez and Ez in W.columns else H.Series(dtype=M);HO=U((Al>0).sum())if not Al.empty else 0;E_=U((Al<0).sum())if not Al.empty else 0;ME=U((Al==0).sum())if not Al.empty else 0;Ov=M(Al.mean())if Al.notna().any()else i;Ow=HO/E_ if E_>0 else D;Ox=M(Al.median())if Al.notna().any()else D;Oy=M(HJ.sum())if HJ.notna().any()else i;Oz=M(HM.sum())if HM.notna().any()else i;O_=M(HN.sum())if HN.notna().any()else i;P0=M(HK.mean())if HK.notna().any()else D;P1=M(HL.mean())if HL.notna().any()else D;MF=U((v>0).sum())if v.notna().any()else 0;MG=U((v<0).sum())if v.notna().any()else 0;HP=0
		if BU and BU in W.columns:HP=U(W[BU].astype(G).str.contains('breakout|buy|bullish',case=J,na=J).sum())
		HQ=0
		if BV and BV in W.columns:HQ=U(W[BV].astype(G).str.contains('buy',case=J,na=J).sum())
		HR,HS=0,0;HT=0
		if AX.notna().any()and BX.notna().any():MH=AX/BX.replace(0,AA.nan)*100;HR=U((MH>=95).sum())
		if AX.notna().any()and A_.notna().any():HU=AX/A_.replace(0,AA.nan)*100;HS=U((HU<=105).sum());HT=U((HU<=115).sum())
		def AY(container,label,value,bg='#f5f7fa',fg='#1a1a1a'):container.markdown(f"<div style='background:{bg}; border-radius:10px; padding:12px 8px; text-align:center; border:1px solid rgba(0,0,0,0.06);'><div style='font-size:0.70em; color:#666; font-weight:700; letter-spacing:0.2px;'>{label}</div><div style='font-size:1.30em; font-weight:800; color:{fg}; margin-top:2px;'>{value}</div></div>",unsafe_allow_html=B)
		BY=A.columns(7);AY(BY[0],'📦 TOTAL STOCKS',f"{MD:,}");AY(BY[1],'🟢 ADVANCES',f"{HO:,}",bg=Ca,fg=GG);AY(BY[2],'🔴 DECLINES',f"{E_:,}",bg=Bp,fg=DE);AY(BY[3],'⚪ UNCHANGED',f"{ME:,}");AY(BY[4],'🕳️ NEAR 52W LOW (≤15%)',f"{HT:,}"if AX.notna().any()and A_.notna().any()else DF,bg=Bp,fg=DE);AY(BY[5],'🚀 BREAKOUTS',f"{HP:,}",bg=GH,fg='#e65100');AY(BY[6],'✅ BUY SIGNALS',f"{HQ:,}",bg=Jv,fg='#0d47a1');A.markdown("<div style='margin-top:8px;'></div>",unsafe_allow_html=B);DZ=A.columns(4);AY(DZ[0],'🏔️ NEAR 52W HIGH (≥95%)',f"{HR:,}",bg=Ca,fg=GG);AY(DZ[1],'🕳️ NEAR 52W LOW (≤5%)',f"{HS:,}",bg=Bp,fg=DE);AY(DZ[2],'📉 BELOW 200 DMA',f"{MG:,}"if v.notna().any()else DF,bg=Bp,fg=DE);AY(DZ[3],'🎯 ABOVE 200 DMA',f"{MF:,}"if v.notna().any()else DF,bg=Ca,fg=GG);A.markdown(Cb,unsafe_allow_html=B);Da={Jw:J,'modeBarButtons':[['toImage']]}
		def MI(frac):
			B=frac;B=AD(i,min(Ar,B));D=[(i,(234,67,53)),(.5,(249,168,37)),(Ar,(15,157,88))]
			for H in Dy(S(D)-1):
				C,A=D[H];E,F=D[H+1]
				if C<=B<=E:G=(B-C)/(E-C)if E>C else i;I=U(A[0]+(F[0]-A[0])*G);J=U(A[1]+(F[1]-A[1])*G);K=U(A[2]+(F[2]-A[2])*G);return f"#{I:02x}{J:02x}{K:02x}"
			return'#999999'
		def P2(title_text,points,y_min,y_max,y_label,height=340):
			G=height;F=y_max;E=points;B=y_min
			if not E:A.info('No data available for this chart.');return
			N=S(E);O=F-B or Ar;H=C
			for(P,(R,I,T))in Dx(E):U=(I-B)/O;K=AD(i,min(Ar,U));V=MI(K);W=P/AD(N-1,1)*100;X=(1-K)*100;H+=f'<a href="{T}" target="_blank" title="{R}: {I:.2f}{y_label}" style="position:absolute; left:{W:.3f}%; top:{X:.3f}%; width:11px; height:11px; margin:-6px 0 0 -6px; border-radius:50%; background:{V}; display:block; border:1px solid rgba(255,255,255,0.75); box-shadow:0 0 1px rgba(0,0,0,0.35); cursor:pointer;"></a>'
			L=C
			for(Y,M)in[(0,F),(25,D),(50,(B+F)/2),(75,D),(100,B)]:Z=f"{M:.0f}"if M is not D else C;L+=f'<div style="position:absolute; left:0; right:0; top:{Y}%; border-top:1px dashed rgba(0,0,0,0.08); height:0;"><span style="position:absolute; left:-2px; top:-8px; font-size:10px; color:#9aa0a6;">{Z}</span></div>'
			a=f'<div style="font-family:\'Source Sans Pro\',sans-serif;"><div style="font-weight:700; font-size:14px; margin-bottom:2px;">{title_text}</div><div style="font-size:11px; color:#9aa0a6; margin-bottom:8px;">Click any dot to open its NSE chart in a new tab</div><div style="position:relative; width:calc(100% - 26px); height:{G}px; margin-left:26px; background:#fff; border:1px solid rgba(0,0,0,0.08); border-radius:6px; overflow:hidden;">{L}{H}</div><div style="display:flex; justify-content:space-between; margin-left:26px; margin-top:4px;"><span style="font-size:10px; color:#ea4335;">● low</span><span style="font-size:10px; color:#f9a825;">● mid</span><span style="font-size:10px; color:#0f9d58;">● high</span></div></div>';Q.html(a,height=G+90,scrolling=J)
		if C1 in W.columns:BZ=W[C1].astype(G)
		elif o in W.columns:BZ=W[o].astype(G)
		else:BZ=W.index.astype(G).to_series(index=W.index)
		if o in W.columns:C2=W[o].astype(G).str.strip()
		else:C2=BZ.astype(G).str.replace('<[^>]+>',C,regex=B).str.strip()
		def HV(fig,chart_key):
			O='customdata';N='points';M='selection';K=chart_key;H=fig;H.update_layout(clickmode='event+select')
			try:I=A.plotly_chart(H,use_container_width=B,key=K,on_select='rerun')
			except Ft:A.plotly_chart(H,use_container_width=B,key=K);A.caption('⚠️ Click-to-open needs Streamlit ≥ 1.35 — update `streamlit` in requirements.txt to enable it.');return
			C=D;F=I.get(M)if B3(I,E)else Fu(I,M,D)
			if F:
				L=F.get(N)if B3(F,E)else Fu(F,N,D)
				if L:
					J=L[-1];G=J.get(O)if B3(J,E)else Fu(J,O,D)
					if G:C=G[0]if B3(G,(AO,tuple))else G
			if C:
				P=f"https://charting.nseindia.com/?symbol={C}-EQ";Q,R=A.columns([3,1])
				with Q:A.success(f"Selected: **{C}**")
				with R:A.link_button('📈 Open on NSE',P,use_container_width=B)
				A.markdown(f"🔗 **More links for {C}:** [TV (🔗)](https://www.tradingview.com/symbols/{C}/) &nbsp;|&nbsp; [TVC (🔗)](https://www.tradingview.com/chart/?symbol=NSE%3A{C}) &nbsp;|&nbsp; [NSE (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={C}) &nbsp;|&nbsp; [NC (🔗)](https://www.charting.nseindia.com/?symbol={C}-EQ) &nbsp;|&nbsp; [CL (🔗)](https://www.chartink.com/stocks-new?symbol={C}) &nbsp;|&nbsp; [CL2 (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={C}) &nbsp;|&nbsp; [Hist (🔗)](https://www.equitypandit.com/historical-data/{C}) &nbsp;|&nbsp; [Scr (🔗)](https://www.screener.in/company/{C}) &nbsp;|&nbsp; [MS (🔗)](https://marketsmithindia.com/mstool/eval/{C}/evaluation.jsp) &nbsp;|&nbsp; [ZK (🔗)](https://zerodha.com/markets/stocks/NSE/{C}) &nbsp;|&nbsp; [WB (🔗)](https://www.whalesbook.com/company/profile/{C}/) &nbsp;|&nbsp; [S (🔗)](https://www.stockanalysis.com/quote/nse/{C}) &nbsp;|&nbsp; [GFi (🔗)](https://www.google.com/finance/beta/quote/{C}:NSE)")
			else:A.caption('Click any dot above to select a stock — its NSE chart button and quick-links will appear here.')
		def MJ(key_prefix):
			W='% Above 52W Low';V='% Below 52W High';C=key_prefix;X,Y=A.columns(2)
			with X:
				if AX.notna().any()and BX.notna().any():G=(BX-AX)/BX.replace(0,AA.nan)*100;I=G.dropna().sort_values(ascending=B).head(30).index;K=H.DataFrame({j:BZ.loc[I].values,V:G.loc[I].values}).iloc[::-1];L=P.Figure(P.Bar(x=K[V],y=K[j],orientation='h',marker_color=A0));L.update_layout(title='🏔️ Top 30 Nearest 52W High',template=u,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(L,use_container_width=B,key=f"{C}_nearhigh_{A4}",config=Da)
				else:A.info('52-Week High column not detected for this sheet.')
			with Y:
				if AX.notna().any()and A_.notna().any():M=(AX-A_)/A_.replace(0,AA.nan)*100;N=M.dropna().sort_values(ascending=B).head(30).index;O=H.DataFrame({j:BZ.loc[N].values,W:M.loc[N].values}).iloc[::-1];Q=P.Figure(P.Bar(x=O[W],y=O[j],orientation='h',marker_color=AS));Q.update_layout(title='🕳️ Top 30 Nearest 52W Low',template=u,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(Q,use_container_width=B,key=f"{C}_nearlow_{A4}",config=Da)
				else:A.info('52-Week Low column not detected for this sheet.')
			Z,a=A.columns(2)
			with Z:
				if v.notna().any():
					R=v[v<0].dropna().sort_values(ascending=B).head(30).index;D=H.DataFrame({j:BZ.loc[R].values,DG:v.loc[R].values}).iloc[::-1]
					if not D.empty:S=P.Figure(P.Bar(x=D[DG],y=D[j],orientation='h',marker_color=AS));S.update_layout(title='📉 Top 30 Below 200 DMA',template=u,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(S,use_container_width=B,key=f"{C}_below200_{A4}",config=Da)
					else:A.info('No stocks currently below 200 DMA.')
				else:A.info(GI)
			with a:
				if v.notna().any():
					T=v[v>0].dropna().sort_values(ascending=J).head(30).index;F=H.DataFrame({j:BZ.loc[T].values,DG:v.loc[T].values}).iloc[::-1]
					if not F.empty:U=P.Figure(P.Bar(x=F[DG],y=F[j],orientation='h',marker_color=A0));U.update_layout(title='🎯 Top 30 Above 200 DMA',template=u,height=780,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(U,use_container_width=B,key=f"{C}_above200_{A4}",config=Da)
					else:A.info('No stocks currently above 200 DMA.')
				else:A.info(GI)
		MJ(EC);MK=A.container();ML=A.container()
		with MK:
			if AX.notna().any()and BX.notna().any()and A_.notna().any():MM=(BX-A_).replace(0,AA.nan);HW=((AX-A_)/MM*100).clip(0,100);HX=HW.notna()&C2.notna();HY=C2[HX].str.strip().values;HZ=HW[HX].values;Ha=P.Figure(P.Scatter(x=HY,y=HZ,mode=ED,marker=E(size=9,color=HZ,colorscale=[[0,AS],[.5,B5],[1,A0]],cmin=0,cmax=100,showscale=B,colorbar=E(title='% of Range')),customdata=HY,hovertemplate=Jx));Ha.update_layout(title='📍 Position within 52-Week Range (0% = Low, 100% = High)',template=u,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=Jy),yaxis_title='% of 52W Range');HV(Ha,f"dash_range_{A4}")
			else:A.info('52-Week High/Low columns not detected for this sheet.')
		with ML:
			if v.notna().any()and C2 is not D:Hb=v.notna()&C2.notna();Hc=C2[Hb].str.strip().values;Db=v[Hb].values;Hd=AD(abs(M(AA.nanmin(Db))),abs(M(AA.nanmax(Db))),1e-09);He=P.Figure(P.Scatter(x=Hc,y=Db,mode=ED,marker=E(size=9,color=Db,colorscale=[[0,AS],[.5,B5],[1,A0]],cmin=-Hd,cmax=Hd,showscale=B,colorbar=E(title='% Diff')),customdata=Hc,hovertemplate=Jx));He.update_layout(title='📐 Difference from 200 DMA (0% = at 200 DMA)',template=u,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=Jy),yaxis_title=DG);HV(He,f"dash_diff200_{A4}")
			else:A.info(GI)
	A.markdown(c);MN,MO,MP=A.columns([3,1,2.2])
	with MN:Hf=A.radio(GJ,[GK,Cc,Cd],horizontal=B,help='Automatically adjust the column widths based on the text length of the selected row.')
	with MP:A.markdown("<div style='margin-top: 2px; font-size:0.9rem;'>🔍 Filter stocks inside this matrix...</div>",unsafe_allow_html=B);Hg=A.text_input(Jz,placeholder=J_,key=JZ,label_visibility='collapsed')
	if Hg:K=K[K[o].astype(G).str.contains(Hg,case=J,na=J)]
	MQ=H0(K);Hh=io.BytesIO()
	with H.ExcelWriter(Hh,engine=DD)as MR:MS=A4[:31].replace(':',C).replace('/',C);MQ.to_excel(MR,index=J,sheet_name=MS)
	with MO:A.markdown("<div style='margin-top: 28px;'></div>",unsafe_allow_html=B);A.download_button(label='📥 Download as Excel',data=Hh.getvalue(),file_name=f"{A4}_Export_{m.now().strftime(Bn)}.xlsx",mime=Bo,use_container_width=J)
	MT,MU=A.columns([1,4])
	with MT:A.write(f"**Rows:** {K.shape[0]} | **Columns:** {S(O)}")
	with MU:MV=A.empty()
	Dc=B8("\n    class HtmlRenderer {\n        init(params) {\n            this.eGui = document.createElement('span');\n            this.eGui.innerHTML = params.value ? String(params.value) : '';\n        }\n        getGui() {\n            return this.eGui;\n        }\n    }\n    ");Hi=B8('\n    function(params) {\n        let colName = params.colDef.field;\n        let c_low = colName.toLowerCase();\n\n        let bgCol = "_bg_" + colName;\n        let txtCol = "_txt_" + colName;\n\n        let bgColor = params.data[bgCol];\n        let txtColor = params.data[txtCol];\n\n        let isTargetCol = c_low.includes("cmp") || c_low.includes("close price") || c_low.includes("prev");\n\n        if (isTargetCol) {\n            if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') return null;\n            return {\n                \'backgroundColor\': bgColor,\n                \'color\': txtColor || \'#000000\',\n                \'fontWeight\': (txtColor === \'#ffffff\' || bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n            };\n        }\n\n        if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') {\n            return { \'color\': \'#000000\' };\n        }\n\n        return {\n            \'backgroundColor\': bgColor,\n            \'color\': \'#000000\',\n            \'fontWeight\': (bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n        };\n    }\n    ');BA=Ea.from_dataframe(K);BA.configure_selection(selection_mode='single',use_checkbox=B);BA.configure_side_bar(filters_panel=J,columns_panel=B);MW=[D5,D6,K0,K1,Ad,G7,EB];Cm=B
	for r in K.columns:
		if r.startswith(Ab)or r.startswith(Ac)or r==o:BA.configure_column(r,hide=B);continue
		if r in Lx:BA.configure_column(r,hide=B);continue
		if Hf==Cc and S(K)>0:
			F0=C0(K.iloc[0][r]);F1=S(G(r));Cn=U(AD(F0,F1)*7+22)
			if Cm:Cn+=30
			Dd,De=Cn,40
		elif Hf==Cd and S(K)>1:
			F0=C0(K.iloc[1][r]);F1=S(G(r));Cn=U(AD(F0,F1)*7+22)
			if Cm:Cn+=30
			Dd,De=Cn,40
		else:Dd,De=(220,150)if r.lower()in MW else(120,80)
		Co=r==C1;Hj=DH if Co or Cm else D
		if Cm:Cm=J
		Hk=r.lower();Hl=BM in Hk;P3='desc'if Hl else D;P4=0 if Hl else D
		if Co or Aa(A in Hk for A in[JM,JN,JO,JP,JQ,JR,JS,'nse']):BA.configure_column(r,width=Dd,minWidth=De,sortable=B,filter=B,resizable=B,editable=J,pinned=Hj,lockPinned=Co,suppressMovable=Co,checkboxSelection=Co,cellRenderer=Dc,cellStyle=Hi)
		else:BA.configure_column(r,width=Dd,minWidth=De,sortable=B,filter=B,resizable=B,editable=J,pinned=Hj,cellStyle=Hi)
	BA.configure_grid_options(domLayout=AT,rowHeight=35,headerHeight=45,enableCellTextSelection=B,ensureDomOrder=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);MX=BA.build();MY=EZ(K,gridOptions=MX,theme=GL,update_mode=L4.SELECTION_CHANGED,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,enable_enterprise_modules=J,height=400,width=GM,key=f"primary_stock_table_grid_{A.session_state.grid_reset_token}");Ba=MY.get('selected_rows',[])
	if Ba is not D and S(Ba)>0 or S(K)>0:
		if Ba is not D and S(Ba)>0:T=Ba.iloc[0]if B3(Ba,H.DataFrame)else Ba[0]
		else:T=K.iloc[0]
		F=G(T.get(o,C)).strip()
		if F:
			with MV.container():A.markdown(f"**⚡ {F} Links:** [TV (🔗)](https://www.tradingview.com/symbols/{F}/) &nbsp;|&nbsp; [TVC (🔗)](https://www.tradingview.com/chart/?symbol=NSE%3A{F}) &nbsp;|&nbsp; [NSE (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={F}) &nbsp;|&nbsp; [NC (🔗)](https://www.charting.nseindia.com/?symbol={F}-EQ) &nbsp;|&nbsp; [% (🔗)](https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern#) &nbsp;|&nbsp; [%K (🔗)](https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern#) &nbsp;|&nbsp; [EQ (🔗)](https://www.nseindia.com/report-detail/eq_security) &nbsp;|&nbsp; [AZ (🔗)](https://https://www.nseindia.com/companies-listing/corporate-filings-application) &nbsp;|&nbsp; [Fin (🔗)](https://https://www.nseindia.com/companies-listing/corporate-filings-financial-results-comparision) &nbsp;|&nbsp; [CL (🔗)](https://www.chartink.com/stocks-new?symbol={F}) &nbsp;|&nbsp; [CL2 (🔗)](https://www.chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={F}) &nbsp;|&nbsp; [History (🔗)](https://www.equitypandit.com/historical-data/{F}) &nbsp;|&nbsp; [Scr(🔗)](https://www.screener.in/company/{F}) &nbsp;|&nbsp; [MS (🔗)](https://marketsmithindia.com/mstool/eval/{F}/evaluation.jsp) &nbsp;|&nbsp; [ZK (🔗)](https://www.zerodha.com/markets/stocks/NSE/{F}) &nbsp;|&nbsp; [WB (🔗)](https://www.whalesbook.com/company/profile/{F}/) &nbsp;|&nbsp; [S (🔗)](https://www.stockanalysis.com/quote/nse/{F}) &nbsp;|&nbsp; [GFi (🔗)](https://www.google.com/finance/beta/quote/{F}:NSE)")
			A.markdown(f"---");A.subheader(f"🛠️ Live Workspace Panel: {F}");AB=A.slider('📏 Adjust Panel Box Height (px):',min_value=300,max_value=1000,value=500,step=50,key='panel_height_slider');AC=A.tabs(['🕯️ Price Chart (EMA + RSI)','📈 Chart & Trade Info (NSE Component)','📋 History Data (EquityPandit)','🎯 Bullish/Bearish Zone','📁 Screener Documents','🪁 Zerodha Portal','📊 MarketSmith India','📉 TradingView Symbol Profile','🤖 AI Stock Analysis','💻 AI Pine Script Builder','🔬 Bottom Fishing Score','🎯 GTT Order Calculator','📊 Watchlist Manager','📰 News Feed'])
			with AC[1]:Hm=f"https://charting.nseindia.com/?symbol={F}-EQ";A.markdown(f"**NSE Interactive Chart Frame** &nbsp;|&nbsp; [🌐 Open in Browser]({Hm})",unsafe_allow_html=J);A.caption(Bq);Q.html(f'<iframe src="{Hm}" width="100%" height="{AB}" style="border:none; border-radius:5px;"></iframe>',height=AB+20)
			with AC[2]:Hn=f"https://www.equitypandit.com/historical-data/{F.lower()}";A.markdown(f"**EquityPandit Historical Matrix Data** &nbsp;|&nbsp; [🌐 Open in Browser]({Hn})");A.caption(Bq);Q.html(f'<iframe src="{Hn}" width="100%" height="{AB}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=AB+20)
			with AC[3]:Ho=f"https://www.equitypandit.com/share-price/{F.lower()}#chart";A.markdown(f"**Bullish / Bearish Zone Indicator** &nbsp;|&nbsp; [🌐 Open in Browser]({Ho})");A.caption(Bq);Q.html(f'<iframe src="{Ho}" width="100%" height="{AB}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=AB+20)
			with AC[4]:Hp=f"https://www.screener.in/company/{F}/consolidated/";A.markdown(f"**Screener Corporate Filings** &nbsp;|&nbsp; [🌐 Open in Browser]({Hp})");A.caption(Bq);Q.html(f'<iframe src="{Hp}" width="100%" height="{AB}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=AB+20)
			with AC[5]:Hq=f"https://zerodha.com/markets/stocks/NSE/{F}/";A.markdown(f"**Zerodha Markets Financial Performance Metrics** &nbsp;|&nbsp; [🌐 Open in Browser]({Hq})");A.caption(Bq);Q.html(f'<iframe src="{Hq}" width="100%" height="{AB}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=AB+20)
			with AC[6]:Hr=f"https://marketsmithindia.com/mstool/eval/{F.lower()}/evaluation.jsp";A.markdown(f"**MarketSmith India Institutional Trading Evaluation Engine** &nbsp;|&nbsp; [🌐 Open in Browser]({Hr})");A.caption(Bq);Q.html(f'<iframe src="{Hr}" width="100%" height="{AB}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=AB+20)
			with AC[7]:Hs=f"https://www.tradingview.com/symbols/{F}/";A.markdown(f"**TradingView Comprehensive Asset Market Registry Summary Profile** &nbsp;|&nbsp; [🌐 Open in Browser]({Hs})");A.caption(Bq);Q.html(f'<iframe src="{Hs}" width="100%" height="{AB}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=AB+20)
			with AC[8]:
				A.markdown(f"### 🤖 Ask AI About **{F}**")
				if not Eb:A.warning(K2)
				else:
					Df=Ed('analysis');A.caption('⚡ Groq = llama-3.3-70b (free, fast) &nbsp;|&nbsp; 🧠 Gemini = gemini-2.5-flash'if BR and Ch else'⚡ Groq connected'if BR else'🧠 Gemini connected');A.write('Using the live data pulled from your dashboard, the AI can analyze technicals, ranges, and context.');F2=A.text_area('Your Query:',value=f"Based on the current data provided, give me a quick summary of the technical performance and trend for {F}.",height=80,key='ai_query_analysis')
					if A.button('✨ Generate AI Analysis',use_container_width=B,key='btn_ai_analysis'):
						with A.spinner(f"Analyzing {F} with {Df}..."):
							try:F3={A:B for(A,B)in T.items()if not G(A).startswith(Br)};Cp=f"""
You are a professional stock market analyst evaluating Indian NSE stocks.
The user is asking about the stock: {F}.

Here is the live data extracted directly from the user's dashboard for this stock:
{F3}

User Query: {F2}

Please provide a clear, concise, and professional response.
""";F4=Ec(Cp,Df);A.session_state[GN]={DI:F,EE:Df,'query':F2,DJ:F4};A.session_state.ai_history.append([F,Df,F2,F4,m.now().strftime(CU)]);A.info(F4)
							except g as Bb:A.error(f"AI error: {Bb}")
					if A.session_state.get(GN,{}).get(DI)==F:
						Cq=A.session_state[GN];Dg=Cq[DJ];A.markdown(c);MZ,Ma,Mb=A.columns(3)
						with MZ:Mc=Eh([[F,Cq[EE],Cq['query'],Dg,m.now().strftime(CU)]]);A.download_button('📥 Save as Excel',data=Mc,file_name=f"AI_{F}_{m.now().strftime(Ju)}.xlsx",mime=Bo,use_container_width=B,key='dl_ai_excel_analysis')
						with Ma:Md=urllib.parse.quote(f"📊 *{F} AI Analysis* ({Cq[EE]})\n\n{Dg[:800]}"+('\n\n_(truncated)_'if S(Dg)>800 else C));A.markdown(f"<a href='https://wa.me/?text={Md}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
						with Mb:Me=urllib.parse.quote(f"📊 {F} AI Analysis ({Cq[EE]})\n\n{Dg[:800]}");A.markdown(f"<a href='https://t.me/share/url?url=NSEDashboard&text={Me}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
					A.markdown(c);A.markdown('**💡 Suggested Prompts** — copy any prompt below and paste it into the query box above:');Mf='\n'.join([f"{A+1}. {B.replace("{sym}",F)}"for(A,B)in Dx(L8)]);A.text(Mf)
			with AC[9]:
				A.markdown(f"### 💻 AI Pine Script Generator for **{F}**")
				if not Eb:A.warning(K2)
				else:
					Mg=Ed('pine');A.write("Generate a custom TradingView Pine Script v5 strategy tailored to this stock's current metrics.");Ht=A.selectbox('Select Strategy Focus:',['Volume Breakout with Dynamic Stop Loss','Moving Average Crossover (50/100/200 DMA)','Trend Following with Trailing Stop','Mean Reversion from 52W High/Low'],key='pine_strategy_focus');Mh=A.text_area('Additional Custom Rules (Optional):',value=f"Include risk management parameters and plot signals on the chart.",height=60,key='pine_query')
					if A.button('⚙️ Generate TradingView Pine Script',use_container_width=B,key='btn_pine'):
						with A.spinner(f"Writing Pine Script v5 code for {F}..."):
							try:F3={A:B for(A,B)in T.items()if not G(A).startswith(Br)};Cp=f'''
You are an expert quantitative developer specializing in TradingView Pine Script v5.

Write a complete, ready-to-copy Pine Script v5 strategy for the stock: {F}.

Strategy Focus: {Ht}
Custom Rules: {Mh}

Here is the live fundamental and technical data for {F} to incorporate as baseline context or threshold values if relevant:
{F3}

Formatting Requirements:
1. Start with `//@version=5` and `strategy("{F} Custom Script", overlay=true)`
2. Include clear comments explaining the logic.
3. Provide ONLY the Pine Script code inside a markdown code block, no other conversational text.
''';Hu=Ec(Cp,Mg);A.session_state[GO]={DI:F,DJ:Hu};A.markdown('### 📋 Your Custom Strategy Code:');A.write('Copy the code below and paste it into the TradingView Pine Editor.');A.markdown(Hu)
							except g as Bb:A.error(f"AI error: {Bb}")
					if A.session_state.get(GO,{}).get(DI)==F:Mi=A.session_state[GO][DJ];Mj=Eh([[F,'Pine Script',Ht,Mi,m.now().strftime(CU)]]);A.download_button('📥 Save Pine Script as Excel',data=Mj,file_name=f"PineScript_{F}_{m.now().strftime(Bn)}.xlsx",mime=Bo,key='dl_pine_excel')
					A.markdown(c);A.markdown('**📋 Custom Rules Reference** — copy any rule and paste it into the Additional Custom Rules box above:');A.text(L9)
			with AC[10]:
				A.markdown(f"### 🔬 Bottom Fishing Analysis: **{F}**");A.caption('Scores this stock on 8 key criteria for buying from the bottom. Based entirely on your live sheet data.');Hv={A:B for(A,B)in T.items()if not G(A).startswith(Br)};C3,F5,F6=DQ(Hv,O);F7=Ae if C3>=75 else Jc if C3>=55 else Jd if C3>=35 else AS;A.markdown(f'''
                <div style="background:{F7}22; border-left:6px solid {F7}; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
                    <div style="font-size:2rem; font-weight:bold; color:{F7};">{C3}/100</div>
                    <div style="font-size:1.3rem; font-weight:bold;">{F5}</div>
                    <div style="font-size:0.85rem; color:#555; margin-top:4px;">Bottom Fishing Composite Score for {F}</div>
                </div>
                ''',unsafe_allow_html=B);A.markdown('#### 📋 Detailed Scoring Breakdown')
				for Mk in F6:A.markdown(f"- {Mk}")
				A.markdown(c);A.markdown('#### 📖 Scoring Criteria');Ml='\n| # | Criteria | Max Points | Description |\n|---|----------|-----------|-------------|\n| 1 | **52W Low Proximity** | 30 | CMP is 8–15% above 52W Low (ideal entry zone) |\n| 2 | **Uptrend (200 DMA)** | 15 | CMP above 200 DMA = confirmed uptrend |\n| 3 | **Volume Activity** | 10 | High trading volume = institutional interest |\n| 4 | **Low/Zero Debt** | 10 | D/E ratio ≤ 0.1 is ideal (no loan burden) |\n| 5 | **Net Profitability** | 10 | Positive net profit confirms fundamental health |\n| 6 | **RONW %** | 10 | Return on Net Worth ≥ 15% = strong business |\n| 7 | **Promoter Holding** | 8 | ≥ 50% shows management confidence |\n| 8 | **Zero Pledge** | 7 | No pledged shares = no financial stress |\n| 9 | **% Delivery** | 10 | ≥ 70% = institutional/genuine buying (not intraday) |\n';A.markdown(Ml);A.info('💡 **Buy Strategy:** Look for scores ≥ 55 (Watchlist) or ≥ 75 (Strong Buy). The sweet zone is CMP at 8–15% above 52W Low with uptrend confirmed (CMP > 200 DMA), backed by positive profits, low debt, and high promoter holding. This combination maximizes probability of a bull run from the bottom.')
				if Eb:
					A.markdown(c);F8=Ed('bf')
					if A.button('🤖 Get AI Deep Analysis for Bottom Buy',use_container_width=B,key='bf_ai_btn'):
						with A.spinner(f"Running deep bottom-fishing analysis for {F} with {F8}..."):
							try:Cp=f"""
You are an expert Indian stock market analyst specializing in bottom-fishing and value investing.

Stock: {F}
Live Data from Dashboard: {Hv}
Bottom Fishing Score: {C3}/100
Grade: {F5}
Scoring Breakdown: {chr(10).join(F6)}

Please provide a comprehensive bottom-fishing analysis covering:
1. Is this stock in or near the 52-week low zone? What does this mean?
2. Is the stock entering an uptrend? Evidence from DMA data.
3. Volume analysis — is there accumulation visible?
4. Fundamental health — debt, profitability, revenue growth signals.
5. Bull run potential — sector tailwinds, promoter activity, institutional interest.
6. Specific entry price zone recommendation with stop loss and target.
7. Risk factors that could delay recovery.
8. Overall verdict: Strong Buy / Watchlist / Avoid for bottom-fishing strategy.

Be specific, data-driven, and actionable for a retail investor.
""";F9=Ec(Cp,F8);A.session_state['last_bf_ai_result']={DI:F,DJ:F9};A.session_state.ai_history.append([F,F8,'Bottom Fishing Deep Analysis',F9,m.now().strftime(CU)]);A.success('✅ AI Analysis Complete');A.markdown(F9)
							except g as Bb:A.error(f"AI error: {Bb}")
					A.markdown(c);A.markdown('#### 📤 Share BF Score Card');Hw=f"""🔬 *Bottom Fishing Score: {F}*

📊 Score: *{C3}/100*
📈 Grade: {F5}

"""+'\n'.join(F6[:5])+f"\n\n🕒 {m.now().strftime(K3)}\n📌 NSE Stock Dashboard";Mm=urllib.parse.quote(Hw);Mn=urllib.parse.quote(Hw);Mo,Mp=A.columns(2)
					with Mo:A.markdown(f"<a href='https://wa.me/?text={Mm}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
					with Mp:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={Mn}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
			with AC[11]:
				A.markdown(f"### 🎯 GTT Order Calculator: **{F}**");A.caption('Auto-suggest Stop-Loss, Targets & ATR-based GTT levels from your live sheet data.');Mq={A:B for(A,B)in T.items()if not G(A).startswith(Br)};AH=Lv(Mq,O)
				if not AH.get(A3):A.warning('⚠️ CMP column not found in sheet data. Cannot compute GTT levels.')
				else:
					V=AH[A3];Mr,Ms,Mt,Mu=A.columns(4);Mr.metric('📍 CMP',f"₹{V:,.2f}")
					if AH.get(G5):Ms.metric('⬆️ 52W High',f"₹{AH[G5]:,.2f}")
					if AH.get(G6):Mt.metric('⬇️ 52W Low',f"₹{AH[G6]:,.2f}")
					if AH.get(EA):Mu.metric('📊 ATR (approx)',f"₹{AH[EA]:,.2f}")
					A.markdown(c);A.markdown('#### ⚙️ Customize ATR Multiplier');Mv,Mw=A.columns(2);Hx=Mv.number_input('Manual ATR Override (₹) — leave 0 to use auto',min_value=i,value=i,step=.5,key='gtt_manual_atr');Dh=Mw.selectbox('Risk-Reward Ratio:',['1:1','1:1.5','1:2','1:2.5','1:3'],index=2,key='gtt_rr_ratio');Mx=M(Dh.split(':')[1]);C4=Hx if Hx>0 else AH.get(EA,0)
					if C4 and C4>0:
						Hy=b(V-Ar*C4,2);C5=b(V-1.5*C4,2);Hz=b(V-2.*C4,2);Di=V-C5;Dj=b(V+Di*Ar,2);Dk=b(V+Di*Mx,2);Dl=b(V+Di*3.,2);My=b(Di/V*100,2);A.markdown('#### 🛡️ Stop-Loss Levels');FA=H.DataFrame([{EF:'Tight SL (1× ATR)',BO:Hy,EG:b((V-Hy)/V*100,2),EH:'Intraday / Scalp'},{EF:'Standard SL (1.5× ATR)',BO:C5,EG:b((V-C5)/V*100,2),EH:'Swing / BTST'},{EF:'Wide SL (2× ATR)',BO:Hz,EG:b((V-Hz)/V*100,2),EH:'Positional'}])
						if AH.get(DC):FA=H.concat([FA,H.DataFrame([{EF:'Trail SL @ 50 DMA',BO:AH[DC],EG:b((V-AH[DC])/V*100,2)if AH[DC]<V else 0,EH:'Trailing Stop'}])],ignore_index=B)
						A.dataframe(FA,use_container_width=B,hide_index=B);A.markdown(f"#### 🎯 Target Levels (based on {Dh} R:R)");Mz=H.DataFrame([{GP:'T1 (1R)',BO:Dj,GQ:b((Dj-V)/V*100,2),GR:'Book 30–40%'},{GP:f"T2 ({Dh} R:R)",BO:Dk,GQ:b((Dk-V)/V*100,2),GR:'Book 40–50%'},{GP:'T3 (3R — runner)',BO:Dl,GQ:b((Dl-V)/V*100,2),GR:'Hold remainder'}]);A.dataframe(Mz,use_container_width=B,hide_index=B);A.markdown('#### 💰 Position Sizing Helper');M_,N0=A.columns(2);N1=M_.number_input('Capital (₹):',min_value=1000,value=100000,step=5000,key='gtt_capital');H_=N0.number_input('Max Risk % of Capital:',min_value=.5,max_value=1e1,value=2.,step=.5,key='gtt_risk_pct');I0=N1*H_/100;FB=U(I0/(V-C5))if V-C5>0 else 0;I1=FB*V;A.success(f"📦 Suggested Qty: **{FB} shares** &nbsp;|&nbsp; Investment: **₹{I1:,.0f}** &nbsp;|&nbsp; Max Loss: **₹{I0:,.0f}** ({H_}%)");A.markdown(c);A.markdown('#### 📋 GTT Order Summary (Copy-Ready)');FC=f"""🎯 *GTT Order: {F}*

📍 Entry CMP: ₹{V:,.2f}
🛡️ Stop-Loss: ₹{C5:,.2f} ({My:.1f}% risk)
🎯 Target 1:  ₹{Dj:,.2f} (+{b((Dj-V)/V*100,1)}%)
🎯 Target 2:  ₹{Dk:,.2f} (+{b((Dk-V)/V*100,1)}%)
🎯 Target 3:  ₹{Dl:,.2f} (+{b((Dl-V)/V*100,1)}%)
📦 Qty: {FB} shares | ₹{I1:,.0f}
📊 ATR: ₹{C4:.2f} | R:R {Dh}
🕒 {m.now().strftime(K3)}""";A.code(FC,language=C);N2=urllib.parse.quote(FC);N3=urllib.parse.quote(FC);N4,N5=A.columns(2)
						with N4:A.markdown(f"<a href='https://wa.me/?text={N2}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share GTT on WhatsApp</button></a>",unsafe_allow_html=B)
						with N5:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={N3}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share GTT on Telegram</button></a>",unsafe_allow_html=B)
					else:A.warning('⚠️ Could not compute ATR — 52W High/Low columns not found in sheet. Please enter ATR manually above.')
			with AC[12]:
				A.markdown(f"### 📊 Watchlist Manager");I2={A:B for(A,B)in T.items()if not G(A).startswith(Br)};N6,N7,_=DQ(I2,O);N8=G(I2.get(q,C))if q else C;FD=F in A.session_state.watchlist;A.markdown(f"**Current Stock: {F}** {"✅ Already in Watchlist"if FD else C}");N9=A.text_input('📝 Note (optional):',value=A.session_state.watchlist.get(F,{}).get(BN,C),placeholder='e.g. Near 52W low, watching for breakout',key=f"wl_note_{F}");NA,NB=A.columns(2)
				with NA:
					if A.button(f"{"🔄 Update"if FD else"➕ Add"} {F} to Watchlist",use_container_width=B,key='wl_add_btn'):
						Lu(F,cmp=N8,note=N9,bf_score=G(N6),bf_grade=N7);NC=Eg()
						if NC:A.success(f"✅ {F} saved to Watchlist (Google Sheet updated!)")
						else:A.info(f"✅ {F} added to session Watchlist (Sheet write failed — check secrets).")
						A.rerun()
				with NB:
					if FD:
						if A.button(f"❌ Remove {F} from Watchlist",use_container_width=B,key='wl_rm_btn'):H5(F);Eg();A.rerun()
				A.markdown(c);A.markdown('#### 🗂️ Your Full Watchlist')
				if A.session_state.watchlist:
					ND=[{j:B,'CMP (₹)':A[A3],D9:A.get(CY,C),GS:A.get(Bm,C),D8:A.get(BN,C),'Added':A.get(DA,C)}for(B,A)in A.session_state.watchlist.items()];I3=H.DataFrame(ND);A.dataframe(I3,use_container_width=B,hide_index=B);I4=io.BytesIO()
					with H.ExcelWriter(I4,engine=DD)as NE:I3.to_excel(NE,index=J,sheet_name=G4)
					A.download_button('📥 Download Watchlist as Excel',data=I4.getvalue(),file_name=f"Watchlist_{m.now().strftime(Bn)}.xlsx",mime=Bo,use_container_width=B,key='dl_wl_excel_tab');NF='\n'.join([f"• {B} — Score:{A.get(CY,C)} {A.get(Bm,C).split()[0]if A.get(Bm)else C} — {A.get(BN,C)[:30]}"for(B,A)in AO(A.session_state.watchlist.items())[:15]]);I5=f"📊 *My NSE Watchlist*\n\n{NF}\n\n🕒 {m.now().strftime(EI)}";NG=urllib.parse.quote(I5);NH=urllib.parse.quote(I5);A.markdown(C);NI,NJ=A.columns(2)
					with NI:A.markdown(f"<a href='https://wa.me/?text={NG}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share Watchlist on WhatsApp</button></a>",unsafe_allow_html=B)
					with NJ:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={NH}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share Watchlist on Telegram</button></a>",unsafe_allow_html=B)
				else:A.info('Your watchlist is empty. Add stocks using the button above!')
			with AC[13]:
				A.markdown(f"### 📰 Latest News & Alerts: **{F}**");import urllib.request,urllib.parse,xml.etree.ElementTree as C6,datetime as m,email.utils
				def NK(pubdate_str):
					try:
						E=email.utils.parsedate_to_datetime(pubdate_str);F=m.datetime.now(m.timezone.utc);G=F-E;A=G.total_seconds()
						if A<0:return AJ
						if A<60:return f"{U(A)} secs ago"
						if A<3600:B=U(A/60);return f"{B} min{"s"if B!=1 else C} ago"
						if A<86400:D=U(A/3600);return f"{D} hour{"s"if D!=1 else C} ago"
						if A<172800:return'Yesterday'
						H=U(A/86400);return f"{H} days ago"
					except g:return GT
				@A.cache_data(ttl=600)
				def NL(target_symbol,limit=10):
					try:
						I=urllib.parse.quote(f'"{target_symbol}" stock share news NSE India');J=f"https://news.google.com/rss/search?q={I}&hl=en-IN&gl=IN&ceid=IN:en";K=urllib.request.Request(J,headers={Ce:Cf})
						with urllib.request.urlopen(K)as M:N=M.read()
						O=C6.fromstring(N);P=[DB,EJ,CX,EK,EL,EM,EN,EO];E=[]
						for A in O.findall(DK):
							F=A.find(A9).text;Q=A.find(f).text;G=A.find(At).text if A.find(At)is not D else C;R=Aa(A in F.lower()for A in P);S=GU if R else C
							try:H=email.utils.parsedate_to_datetime(G)
							except g:H=m.datetime.min.replace(tzinfo=m.timezone.utc)
							E.append({AF:f"{S}{F}",f:Q,L:NK(G),AK:H})
						E.sort(key=lambda x:x[AK],reverse=B);return E[:limit]
					except g:return[]
				with A.spinner(f"Fetching today's latest news for {F}..."):
					I6=NL(F,limit=10)
					if I6:
						for N in I6:h=Af in N[L]or Ag in N[L]or Ah in N[L]or AJ in N[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.5em 0; opacity: 0.2;'>",unsafe_allow_html=B)
					else:A.info(f"No recent news found for {F}.")
			with AC[0]:
				with A.expander(f"🕯️ Price Chart & Technical Indicators — {F}",expanded=B):
					NM=A.select_slider('History range:',options=['1doy','3mo','6mo','1y','2y','5y'],value='1y',key=f"chart_period_{F}")
					with A.spinner(f"Loading price history for {F}..."):n=LT(F,period=NM)
					if n.empty or BJ not in n.columns:A.warning(f"⚠️ No historical price data available for **{F}** via Yahoo Finance (tried `{F}.NS`). The symbol may be delisted, renamed, or not tracked by Yahoo.")
					else:
						Am=n[BJ].squeeze().dropna();AN=M(Am.iloc[-1]);Bc=M(Am.iloc[-2])if S(Am)>1 else AN;Dm=(AN-Bc)/Bc*100 if Bc else i;I7=Am.diff();NN=I7.clip(lower=0).rolling(14).mean();NO=(-I7.clip(upper=0)).rolling(14).mean();FE=100-100/(1+NN/NO.replace(0,M(A8)));Cr=FE.dropna().iloc[-1]if not FE.dropna().empty else D;NP,NQ=A.tabs(['Price + EMAs','RSI'])
						with NP:
							NR=A.radio('Chart type',[K4,'Line'],horizontal=B,key=f"chart_type_{F}");I8=Am.diff();NS=I8.clip(lower=0).rolling(9).mean();NT=(-I8.clip(upper=0)).rolling(9).mean();B0=100-100/(1+NS/NT.replace(0,M(A8)));FF=B0.ewm(span=3,adjust=J).mean();I9=AA.arange(1,22,dtype=M);FG=B0.rolling(21).apply(lambda x:M(AA.dot(x,I9)/I9.sum()),raw=B);y=AO(n.index);IA=B0.values;Cs,IB=[],[];FH,IC=[],[]
							for BS in Dy(22,S(B0)):
								FI,ID=IA[BS],IA[BS-1]
								if AA.isnan(FI)or AA.isnan(ID):continue
								if FI>=50 and ID<50:
									Dn=B0.index[BS]
									if Dn in Am.index:Cs.append(Dn);IB.append(M(Am.loc[Dn])*.993);FH.append(Dn);IC.append(M(FI))
							if not FF.dropna().empty and not FG.dropna().empty:FJ=FF.dropna().iloc[-1];FK=FG.dropna().iloc[-1];FL=GV if FJ>FK else GW;NU='🟢 H-M: POSITIVE (Bullish)'if FJ>FK else'🔴 H-M: NEGATIVE (Bearish)';A.markdown(f"<div style='background:{FL}22;border-left:4px solid {FL};padding:6px 12px;border-radius:4px;margin-bottom:6px;font-size:13px;font-weight:700;color:{FL}'>{NU} — EMA3: {FJ:.1f} | WMA21: {FK:.1f}</div>",unsafe_allow_html=B)
							e=L5(rows=3,cols=1,shared_xaxes=B,row_heights=[.55,.25,.2],vertical_spacing=.03,specs=[[{GX:'xy'}],[{GX:'xy'}],[{GX:'xy'}]])
							if NR==K4:
								try:e.add_trace(P.Candlestick(x=y,open=n['Open'].squeeze(),high=n[EP].squeeze(),low=n[EQ].squeeze(),close=n[BJ].squeeze(),name='OHLC',increasing_line_color=GY,decreasing_line_color=GZ,increasing_fillcolor=GY,decreasing_fillcolor=GZ,line=E(width=1.6),whiskerwidth=.9),row=1,col=1)
								except g:e.add_trace(P.Scatter(x=y,y=Am,name=BJ,line=E(color=AG,width=2)),row=1,col=1)
							else:e.add_trace(P.Scatter(x=y,y=Am,name=BJ,line=E(color=AG,width=2)),row=1,col=1)
							for(NV,NW,NX)in[(20,K5,'EMA20'),(50,'#FF6D00','EMA50'),(200,'#2979FF','EMA200')]:NY=Am.ewm(span=NV,adjust=J).mean();e.add_trace(P.Scatter(x=y,y=NY,name=NX,line=E(color=NW,width=1.8)),row=1,col=1)
							IE=M(n[EP].max());IF=M(n[EQ].min());e.add_hline(y=IE,line_dash=EC,line_color=K6,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W High ₹{IE:,.2f}",annotation_position=K7,annotation_font=E(color=K6,size=13));e.add_hline(y=IF,line_dash=EC,line_color=K8,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W Low ₹{IF:,.2f}",annotation_position='bottom right',annotation_font=E(color=K8,size=13))
							if Cs:e.add_trace(P.Scatter(x=Cs,y=IB,mode=ED,name='H-M Entry (RSI>50)',marker=E(color='lime',size=12,symbol=K9,line=E(color='white',width=1.5))),row=1,col=1)
							try:IG=n[s].squeeze();NZ=n['Open'].squeeze();Na=n[BJ].squeeze();Nb=[GY if B>=A else GZ for(A,B)in zip(NZ.tolist(),Na.tolist())];e.add_trace(P.Bar(x=y,y=IG.tolist(),name=s,marker=E(color=Nb,line=E(width=0)),opacity=.85,showlegend=J),row=3,col=1);Nc=IG.rolling(20).mean();e.add_trace(P.Scatter(x=y,y=Nc.tolist(),name='Vol Avg(20)',line=E(color='#616161',width=1.2,dash=DL)),row=3,col=1)
							except g:pass
							Do=B0.reindex(B0.index);IH=H.Series(5e1,index=B0.index);Nd=Do.where(Do>=50,5e1);e.add_trace(P.Scatter(x=y,y=IH.tolist(),line=E(width=0),mode=ER,showlegend=J,hoverinfo=ES),row=2,col=1);e.add_trace(P.Scatter(x=y,y=Nd.tolist(),fill=KA,fillcolor='rgba(38,166,154,0.35)',line=E(width=0),mode=ER,showlegend=J,hoverinfo=ES),row=2,col=1);Ne=Do.where(Do<=50,5e1);e.add_trace(P.Scatter(x=y,y=IH.tolist(),line=E(width=0),mode=ER,showlegend=J,hoverinfo=ES),row=2,col=1);e.add_trace(P.Scatter(x=y,y=Ne.tolist(),fill=KA,fillcolor='rgba(239,83,80,0.35)',line=E(width=0),mode=ER,showlegend=J,hoverinfo=ES),row=2,col=1);e.add_trace(P.Scatter(x=y,y=B0.tolist(),name='RSI(9)',line=E(color='#1976D2',width=1.5)),row=2,col=1);e.add_trace(P.Scatter(x=y,y=FF.tolist(),name='EMA3',line=E(color='#4CAF50',width=1.5)),row=2,col=1);e.add_trace(P.Scatter(x=y,y=FG.tolist(),name='WMA21',line=E(color='#EF5350',width=1.5)),row=2,col=1)
							if FH:e.add_trace(P.Scatter(x=FH,y=IC,mode=ED,name='Entry (RSI panel)',showlegend=J,marker=E(color='lime',size=6,symbol=K9,line=E(color='white',width=1))),row=2,col=1)
							e.add_hline(y=70,line_dash=DL,line_color=GW,opacity=.5,row=2,col=1);e.add_hline(y=50,line_dash=EC,line_color='#888888',row=2,col=1,annotation_text='50',annotation_position='right');e.add_hline(y=30,line_dash=DL,line_color=K5,opacity=.8,row=2,col=1,annotation_text='30',annotation_position='right');e.update_layout(template=u,height=950,title=E(text=f"{F} — Ultra HD Chart (Price, EMAs, H-M, Volume)",font=E(size=12,color='#0E1117',family=ET)),margin=E(t=60,b=80,l=20,r=20),xaxis_rangeslider_visible=J,xaxis2_rangeslider_visible=J,xaxis3_rangeslider_visible=J,legend=E(orientation='h',y=-.15,x=.5,xanchor='center',yanchor='top',font=E(size=13,color=KB,family=ET)),hovermode='x unified',font=E(size=13,color=KB,family=ET),hoverlabel=E(font_size=14,font_family=ET,bgcolor='rgba(255,255,255,0.95)'),plot_bgcolor=EU,paper_bgcolor=EU,bargap=.15);e.update_xaxes(showspikes=B,spikemode='across+toaxis',spikesnap='cursor',spikethickness=1.5,spikedash='solid',spikecolor='#808495',gridcolor=KC,linecolor=Ga,tickfont=E(size=12,family=KD));e.update_yaxes(gridcolor=KC,zeroline=J,linecolor=Ga,tickfont=E(size=12,family=KD));e.update_yaxes(range=[0,100],row=2,col=1);e.update_yaxes(title_text=BO,title_font=E(size=14,weight=AU),row=1,col=1);e.update_yaxes(title_text='RSI / H-M',title_font=E(size=14,weight=AU),row=2,col=1);e.update_yaxes(title_text=s,title_font=E(size=14,weight=AU),row=3,col=1);Nf={Jw:J,'responsive':B,'toImageButtonOptions':{'format':'png','filename':f"{F}_Ultra_HD_Analysis",'height':1080,'width':1920,'scale':6},'modeBarButtonsToAdd':['drawline','drawopenpath','drawrect','eraseshape']};A.plotly_chart(e,use_container_width=B,key=f"price_ema_chart_{F}",config=Nf)
							if Cs:A.caption(f"🟢 {S(Cs)} H-M entry signal(s) — RSI(9) crossed above 50 (bottom-catch). **H-M panel:** Green fill = RSI above 50 (momentum). Red fill = RSI below 50 (pullback). For informational purposes only.")
							else:A.caption('**H-M panel:** Green fill = RSI above 50. Red fill = RSI below 50 (pullback zone). 🟢 circles = RSI(9) cross above 50 (entry). For informational purposes only.')
							X={}
							if A4!=BI:
								Dp=DO(BI)
								if not Dp.empty:
									Ng=[A for A in Dp.columns if not A.startswith(Ab)and not A.startswith(Ac)];II=R((A for A in Ng if A.lower()in[D5,Ad,E1,E2,D6,E3]),D)
									if II:
										IJ=Dp[Dp[II].astype(G).str.strip()==F]
										if not IJ.empty:Nh=IJ.iloc[0].to_dict();X={A:B for(A,B)in Nh.items()if not G(A).startswith(Ab)and not G(A).startswith(Ac)and G(A)!=o}
							def Y(row,primary_dict,*K):
								def B(r_data):
									J='n/a';B=r_data
									if B is D or S(B)==0:return l
									try:H=AO(B.keys())if B3(B,E)else AO(B.index)
									except g:return l
									H=[A for A in H if not G(A).startswith(Ab)and not G(A).startswith(Ac)and G(A)!=o]
									for L in K:
										I=L.lower().strip()
										for F in H:
											if G(F).strip().lower()==I:
												A=B.get(F,C);A=C if A is D else G(A).strip()
												if A not in(C,A8,AR,DF,J,l):return A
										for F in H:
											if I in G(F).strip().lower():
												A=B.get(F,C);A=C if A is D else G(A).strip()
												if A not in(C,A8,AR,DF,J,l):return A
									return l
								A=B(primary_dict)
								if A==l:A=B(row)
								return A
							def IK(label,value):return f"<div style='background:var(--secondary-background-color,#F0F2F6);border:1px solid rgba(128,128,128,0.35);border-radius:6px;padding:8px 10px;min-width:150px;flex:1 1 150px;'><div style='font-size:11px;color:var(--text-color,#31333F);opacity:0.65;margin-bottom:3px;'>{label}</div><div style='font-size:14px;font-weight:700;color:var(--text-color,#0E1117);word-break:break-word;'>{value}</div></div>"
							def FM(title,fields):D=C.join(IK(A,Y(T,X,*B))for(A,B)in fields);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
						with NQ:Ni=AO(n.index);BB=P.Figure();BB.add_trace(P.Scatter(x=Ni,y=FE,name=KE,line=E(color='#AB47BC',width=2)));BB.add_hline(y=70,line_dash=DL,line_color=GW,opacity=.6);BB.add_hline(y=30,line_dash=DL,line_color=GV,opacity=.6);BB.add_hrect(y0=45,y1=65,fillcolor=GV,opacity=.06,line_width=0,annotation_text='Ideal entry 45-65',annotation_position=K7);BB.update_layout(template=u,height=280,yaxis=E(range=[0,100]),margin=E(t=30,b=20),plot_bgcolor=EU,paper_bgcolor=EU,font=E(color='#1A1A1A'));BB.update_xaxes(gridcolor=KF);BB.update_yaxes(gridcolor=KF);A.plotly_chart(BB,use_container_width=B,key=f"rsi14_chart_{F}")
				A.markdown("<hr style='margin:16px 0 4px 0;opacity:0.25;'>",unsafe_allow_html=B)
				with A.expander(f"📋 {F} — Google Sheet Data",expanded=B):
					def Nj(title,items):D=C.join(IK(A,B)for(A,B)in items);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
					Nk='▲'if Dm>=0 else'▼';Nl='#00A152'if Dm>=0 else'#D32F2F';Nj('📊 Price Snapshot',[(KG,f"₹{AN:,.2f} <span style='color:{Nl};font-size:12px;'>{Nk} {Dm:+.2f}%</span>"),(Ap,f"₹{M(n[EP].max()):,.2f}"),(Aq,f"₹{M(n[EQ].min()):,.2f}"),(KE,f"{Cr:.1f}"if Cr is not D else'–')])
					with A.expander('📋 Company Price Dashboard',expanded=J):FM('🏢 Company Info',[('Company Name',[K0,K1]),(Gb,[EB,G7]),(Ao,[G3,KH,BM]),('52W High Date',[Js,'52 week high date']),('52W Low Date',[Jt,'52 week low date']),(s,[BL]),(D7,[Bl])]);FM('📡 Signals & System Output',[(JH,[Jf]),('Difference from 200 DMA',['difference from 200 dma','differance from 200 dma']),('CAR Rating',['cumulative average rule (car) rating','car rating']),('Start GTT Order',[Jg,'gtt order']),(Bs,[G8]),(Bt,[G9]),(Bu,[GA]),(Bv,[Jh]),(Bw,[GB])]);FM('💰 Fundamentals',[(Jp,['face value']),('Total Equity Capital',[Gc]),(Jr,[GF]),('EPS',['eps']),(Jq,['ronw']),(Jn,[F_,G0]),(Jo,[KI,KJ]),('Pledged %',[G1,G2]),('D/E Ratio',[JW,'de ratio']),('Net Sales (Cr)',[E7]),('Net Profit (Cr.)',[E6]),('Reserves (Cr)',[Gd]),('Total Debt (Cr)',[Ge]),('Inventory (Cr)',[Gf]),('Cash & Equiv (Cr)',[Gg,Gh,Gi]),('Operating Cash Flow (Cr)',['operating cash flow']),('Trade Receivables (Cr)',[Gj]),('Trade Payables (Cr)',[Gk]),('Fixed Assets/Net PPE (Cr)',[Gl,Gm]),('Total Assets (Cr)',[Gn]),('Open (₹)',['open price','open (','open']),('High (₹)',['day high','high price','high (']),('Low (₹)',['day low','low price','low (']),('Prev Close (₹)',['prev close','previous close',GE]),('Price Change (₹)',['price change','change (','change in price']),('% Change',['% change',CV,'change %']),('Shares Outstanding (Cr)',['shares outstanding']),('Book Value (₹/share)',['book value']),('Public %',['public %','public holding']),('FII %',['fii %','fii holding','fii']),('DII %',['dii %','dii holding','dii'])])
					def d(raw):
						if raw in(D,l,C,A8,AR):return
						try:return M(G(raw).replace(AE,C).replace('₹',C).strip())
						except(AZ,Ft):return
					def A5(h,alpha=.35):return f"rgba({U(h[1:3],16)},{U(h[3:5],16)},{U(h[5:7],16)},{alpha})"
					if Bc and AN is not D:IL=AN-Bc;IM=P.Figure(P.Waterfall(orientation='v',measure=['absolute','relative','total'],x=['Prev Close','Change',KG],y=[Bc,IL,AN],text=[f"₹{Bc:,.2f}",f"{IL:+.2f}",f"₹{AN:,.2f}"],textposition='outside',textfont=E(color=Au,size=13),increasing=E(marker=E(color=A0)),decreasing=E(marker=E(color=AS)),totals=E(marker=E(color=AG)),connector=E(line=E(color=Ga))));IM.update_layout(title=f"📈 Price Change Bridge — {F} ({Dm:+.2f}%)",template=u,height=300,showlegend=J,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IM,use_container_width=B,key=f"waterfall_price_{F}");A.caption("Prev Close → today's Price Change → Last Close. Shown as a Waterfall, not a Sankey, since a price drop can't be a negative flow.")
					else:A.info("Prev Close / Last Close not available for this stock, so the Price Change bridge can't be built.")
					Nm=Y(T,X,BL);An=d(Y(T,X,G3,KH,BM));C7=d(Nm)
					if C7 is not D and An is not D and 0<=An<=100:FN=C7*An/100;IN=C7-FN;IO=P.Figure(P.Sankey(arrangement=Bx,textfont=E(color=Au,size=13,family=By),node=E(pad=30,thickness=18,line=E(color=Bz,width=.5),label=[f"Volume<br>{C7:,.0f} shares",f"Delivered<br>{FN:,.0f} shares ({An:.1f}%)",f"Intraday / Non-Delivery<br>{IN:,.0f} shares ({100-An:.1f}%)"],color=[Cg,A0,B5]),link=E(source=[0,0],target=[1,2],value=[FN,IN],color=[A5(A0),A5(B5)])));IO.update_layout(title=f"📦 Volume → Delivery Split — {F}",template=u,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IO,use_container_width=B,key=f"sankey_volume_{F}");A.caption('Total Volume split by % Delivery into shares actually delivered (genuine buying/holding) vs. shares traded intraday and squared off same day.')
					else:A.info("Volume / % Delivery not available for this stock, so the Volume → Delivery split can't be built.")
					if Cr is not D:IP=P.Figure(P.Indicator(mode=KK,value=M(Cr),number=E(font=E(color=Au,size=28)),title=E(text=f"RSI(14) — {F}",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AG),steps=[E(range=[0,30],color=Jv),E(range=[30,70],color='#f5f5f5'),E(range=[70,100],color=Bp)],threshold=E(line=E(color=DM,width=3),value=M(Cr)))));IP.update_layout(template=u,height=260,margin=E(t=50,b=10,l=30,r=30));A.plotly_chart(IP,use_container_width=B,key=f"gauge_rsi_{F}");A.caption("Below 30 = oversold, above 70 = overbought. A gauge, not a Sankey — RSI doesn't split into parts.")
					else:A.info('RSI(14) not available for this stock.')
					Dq=M(n[EP].max())if not n.empty else D;Ct=M(n[EQ].min())if not n.empty else D
					if Dq and Ct is not D and Dq>Ct and AN is not D:IQ=AD(i,min(1e2,(AN-Ct)/(Dq-Ct)*100));IR=P.Figure(P.Indicator(mode=KK,value=IQ,number=E(suffix=t,font=E(color=Au,size=28)),title=E(text=f"52W Range Position — {F}<br><span style='font-size:11px'>Low ₹{Ct:,.2f} · Last ₹{AN:,.2f} · High ₹{Dq:,.2f}</span>",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AG),steps=[E(range=[0,33],color=Bp),E(range=[33,66],color=GH),E(range=[66,100],color=Ca)],threshold=E(line=E(color=DM,width=3),value=IQ))));IR.update_layout(template=u,height=280,margin=E(t=65,b=10,l=30,r=30));A.plotly_chart(IR,use_container_width=B,key=f"gauge_52wrange_{F}");A.caption("0% = at the 52-week low, 100% = at the 52-week high. A gauge, not a Sankey — price levels aren't a splittable quantity.")
					else:A.info('52-week High/Low/Last Close not available for this stock.')
					C8=d(Y(T,X,Bl));FO=J
					if C8 is D and C7 is not D and AN:C8=C7*AN/1e7;FO=B
					if C8 is not D and An is not D and 0<=An<=100:FP=C8*An/100;IS=C8-FP;IT=P.Figure(P.Sankey(arrangement=Bx,textfont=E(color=Au,size=13,family=By),node=E(pad=30,thickness=18,line=E(color=Bz,width=.5),label=[f"{"Est. "if FO else C}Turnover<br>₹{C8:,.2f} Cr",f"Delivered Value<br>₹{FP:,.2f} Cr ({An:.1f}%)",f"Intraday Value<br>₹{IS:,.2f} Cr ({100-An:.1f}%)"],color=[Cg,A0,B5]),link=E(source=[0,0],target=[1,2],value=[FP,IS],color=[A5(A0),A5(B5)])));IT.update_layout(title=f"💵 Turnover → Delivery Split — {F}",template=u,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IT,use_container_width=B,key=f"sankey_turnover_{F}");Nn=" Your sheet's Turnover field is blank for this stock, so this uses an estimate (Volume × Last Close) — the same fallback this app already uses elsewhere."if FO else C;A.caption(f"Turnover split by % Delivery, mirroring the Volume split above in ₹ terms.{Nn}")
					else:A.info("Turnover / % Delivery / Volume not available for this stock, so the Turnover → Delivery split can't be built.")
					C9=d(Y(T,X,GF));CA=d(Y(T,X,F_,G0));CB=d(Y(T,X,KI,KJ));FQ=d(Y(T,X,G1,G2))
					if C9 is not D and C9>0 and(CA is not D or CB is not D):
						CA=CA or i;CB=CB or i;IU=AD(i,1e2-CA-CB);Cu=C9*CA/100;IV=C9*CB/100;IW=C9*IU/100;IX=[f"Market Cap<br>₹{C9:,.2f} Cr",f"Promoters<br>₹{Cu:,.2f} Cr ({CA:.1f}%)",f"Institutional<br>₹{IV:,.2f} Cr ({CB:.1f}%)",f"Public / Other<br>₹{IW:,.2f} Cr ({IU:.1f}%)"];IY=[Cg,AG,A0,EV];IZ=[0,0,0];Ia=[1,2,3];Ib=[Cu,IV,IW];Ic=[A5(A)for A in[AG,A0,EV]];Id=C
						if FQ is not D and Cu>0:FR=Cu*FQ/100;Ie=Cu-FR;IX+=[f"Pledged (of Promoters)<br>₹{FR:,.2f} Cr ({FQ:.1f}%)",f"Free / Unpledged<br>₹{Ie:,.2f} Cr"];IY+=[DM,D2];IZ+=[1,1];Ia+=[4,5];Ib+=[FR,Ie];Ic+=[A5(DM),A5(D2)];Id=" Promoters' holding is further split into Pledged vs Free based on Pledged %."
						If=P.Figure(P.Sankey(arrangement=Bx,textfont=E(color=Au,size=13,family=By),node=E(pad=30,thickness=18,line=E(color=Bz,width=.5),label=IX,color=IY),link=E(source=IZ,target=Ia,value=Ib,color=Ic)));If.update_layout(title=f"🧾 Shareholding Pattern — Who Owns {F}",template=u,height=380,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(If,use_container_width=B,key=f"sankey_shareholding_{F}");A.caption(f'Market Cap × holding % from the Fundamentals data above. "Public / Other" absorbs whatever isn\'t reported as Promoters/Institutional (Public %, FII %, DII % show "-" for stocks where your sheet doesn\'t break those out separately).{Id}')
					else:A.info("Market Cap / shareholding % data not available for this stock, so the Shareholding Pattern flow can't be built.")
					Bd=d(Y(T,X,E7));BC=d(Y(T,X,E6))
					if Bd is not D and BC is not D and 0<BC<Bd:Ig=Bd-BC;FS=BC/Bd*100;Ih=P.Figure(P.Sankey(arrangement=Bx,textfont=E(color=Au,size=13,family=By),node=E(pad=30,thickness=18,line=E(color=Bz,width=.5),label=[f"Net Sales<br>₹{Bd:,.2f} Cr (100%)",f"Net Profit<br>₹{BC:,.2f} Cr ({FS:.1f}%)",f"Total Expenses<br>₹{Ig:,.2f} Cr ({100-FS:.1f}%)"],color=[AG,A0,AS]),link=E(source=[0,0],target=[1,2],value=[BC,Ig],color=['rgba(15,157,88,0.35)','rgba(234,67,53,0.35)'])));Ih.update_layout(title=f"💰 Revenue & Expenses Flow — {F} (Net Margin {FS:.1f}%)",template=u,height=320,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ih,use_container_width=B,key=f"sankey_{F}");A.caption('Based on Net Sales / Net Profit from the Fundamentals data above. "Total Expenses" is the remainder (Net Sales − Net Profit) — your sheet doesn\'t carry a Cost-of-Revenue/Opex breakdown, so a multi-stage flow (Gross → Operating → Net) isn\'t available for this stock.')
					elif Bd is not D and BC is not D:A.info(f"Revenue & Expenses flow needs a normal profitable split (0 < Net Profit < Net Sales). {F} currently shows Net Sales ₹{Bd:,.2f} Cr and Net Profit ₹{BC:,.2f} Cr, which doesn't fit a simple flow diagram (e.g. a net loss).")
					else:A.info("Net Sales / Net Profit not available for this stock, so the Revenue & Expenses flow can't be built.")
					No=d(Y(T,X,Gc));Np=d(Y(T,X,Gd));Nq=d(Y(T,X,Ge));Nr=d(Y(T,X,Gk));Ns=[(KL,No,AG),(KM,Np,A0),(KN,Nq,AS),(KO,Nr,KP)];BD=[(B,A,C)for(B,A,C)in Ns if A is not D and A>0]
					if S(BD)>=2:Ii=sum(B for(A,B,A)in BD);Ij=P.Figure(P.Sankey(arrangement=Bx,textfont=E(color=Au,size=13,family=By),node=E(pad=30,thickness=18,line=E(color=Bz,width=.5),label=[f"Total Financing<br>₹{Ii:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/Ii*100:.1f}%)"for(B,A,C)in BD],color=[KQ]+[B for(A,A,B)in BD]),link=E(source=[0]*S(BD),target=AO(Dy(1,S(BD)+1)),value=[B for(A,B,A)in BD],color=[A5(B)for(A,A,B)in BD])));Ij.update_layout(title=f"🏗️ Capital Structure — How {F} Is Financed",template=u,height=300,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ij,use_container_width=B,key=f"sankey_capstruct_{F}");A.caption('Equity Capital + Reserves + Total Debt + Trade Payables, from the Fundamentals data above.')
					else:A.info('Not enough of Total Equity Capital / Reserves / Total Debt / Trade Payables available to build a Capital Structure flow.')
					CC=d(Y(T,X,Gn));Nt=[(KR,d(Y(T,X,Gl,Gm)),KS),(KT,d(Y(T,X,Gf)),B5),(KU,d(Y(T,X,Gj)),KV),(KW,d(Y(T,X,Gg,Gh,Gi)),AG)];FT=[(B,A,C)for(B,A,C)in Nt if A is not D and A>=0]
					if CC is not D and CC>0 and FT:
						Ik=sum(B for(A,B,A)in FT);FU=CC-Ik
						if FU>=0:CD=FT+([(KX,FU,EV)]if FU>0 else[]);Il=P.Figure(P.Sankey(arrangement=Bx,textfont=E(color=Au,size=13,family=By),node=E(pad=30,thickness=18,line=E(color=Bz,width=.5),label=[f"Total Assets<br>₹{CC:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/CC*100:.1f}%)"for(B,A,C)in CD],color=[Cg]+[B for(A,A,B)in CD]),link=E(source=[0]*S(CD),target=AO(Dy(1,S(CD)+1)),value=[B for(A,B,A)in CD],color=[A5(B)for(A,A,B)in CD])));Il.update_layout(title=f"📦 Asset Deployment — Where {F}'s Assets Sit",template=u,height=340,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Il,use_container_width=B,key=f"sankey_assets_{F}");A.caption('Fixed Assets, Inventory, Trade Receivables and Cash & Equivalents from the Fundamentals data above. "Other Assets" is the gap versus reported Total Assets (e.g. intangibles, investments, or other items your sheet doesn\'t itemize).')
						else:A.info(f"{F}'s itemized asset categories (₹{Ik:,.2f} Cr) add up to more than the reported Total Assets (₹{CC:,.2f} Cr) — likely a data mismatch between sheet rows, so the Asset Deployment flow isn't shown to avoid a misleading chart.")
					else:A.info("Total Assets / asset-category data not available for this stock, so the Asset Deployment flow can't be built.")
					FV,Im,Dr=[],[],[];CE,CF,CG,CH=[],[],[],[]
					def Be(label,color,col_x):FV.append(label);Im.append(color);Dr.append(col_x);return S(FV)-1
					Nu,Nv,In,FW=.001,.24,.5,.999;Nw=[(KL,d(Y(T,X,Gc)),AG),(KM,d(Y(T,X,Gd)),A0),(KN,d(Y(T,X,Ge)),AS),(KO,d(Y(T,X,Gk)),KP)];FX=[(B,A,C)for(B,A,C)in Nw if A is not D and A>0];Io=S(FX)>=2;BE=D
					if Io:
						Ds=sum(B for(A,B,A)in FX);BE=Be(f"Total Financing<br>₹{Ds:,.2f} Cr (100%)",KQ,Nv)
						for(B1,AI,Cv)in FX:y=Be(f"{B1}<br>₹{AI:,.2f} Cr ({AI/Ds*100:.1f}%)",Cv,Nu);CE.append(y);CF.append(BE);CG.append(AI);CH.append(A5(Cv))
					Bf=d(Y(T,X,Gn));Nx=[(KR,d(Y(T,X,Gl,Gm)),KS),(KT,d(Y(T,X,Gf)),B5),(KU,d(Y(T,X,Gj)),KV),(KW,d(Y(T,X,Gg,Gh,Gi)),AG)];FY=[(B,A,C)for(B,A,C)in Nx if A is not D and A>=0];Dt=Bf is not D and Bf>0 and bool(FY)
					if Dt:Ny=sum(B for(A,B,A)in FY);FZ=Bf-Ny;Dt=FZ>=0
					if Dt:
						Nz=FY+([(KX,FZ,EV)]if FZ>0 else[]);N_=f" ({Bf/Ds*100:.1f}%)"if BE is not D else KY;Ip=Be(f"Total Assets<br>₹{Bf:,.2f} Cr{N_}",Cg,In)
						if BE is not D:CE.append(BE);CF.append(Ip);CG.append(Bf);CH.append(A5(Cg))
						for(B1,AI,Cv)in Nz:y=Be(f"{B1}<br>₹{AI:,.2f} Cr ({AI/Bf*100:.1f}%)",Cv,FW);CE.append(Ip);CF.append(y);CG.append(AI);CH.append(A5(Cv))
					Bg=d(Y(T,X,E7));CI=d(Y(T,X,E6));Iq=Bg is not D and CI is not D and 0<CI<Bg
					if Iq:
						Ir=Bg-CI;O0=f" ({Bg/Ds*100:.1f}%)"if BE is not D else KY;Fa=Be(f"Net Sales<br>₹{Bg:,.2f} Cr{O0}",AG,In)
						if BE is not D:CE.append(BE);CF.append(Fa);CG.append(Bg);CH.append(A5(AG))
						Is=CI/Bg*100;O1=Be(f"Net Profit<br>₹{CI:,.2f} Cr ({Is:.1f}%)",A0,FW);O2=Be(f"Total Expenses<br>₹{Ir:,.2f} Cr ({100-Is:.1f}%)",AS,FW);CE+=[Fa,Fa];CF+=[O1,O2];CG+=[CI,Ir];CH+=[A5(A0),A5(AS)]
					O3=sum([Io,Dt,Iq])
					if O3>0:
						from collections import defaultdict as It;Iu=It(U)
						for Cw in Dr:Iu[Cw]+=1
						Iv=It(U);Iw=[]
						for Cw in Dr:B1=Iu[Cw];BS=Iv[Cw];Iv[Cw]+=1;Iw.append(b((BS+.5)/B1,4)if B1>1 else .5)
						Ix=P.Figure(P.Sankey(arrangement=Bx,textfont=E(color=Au,size=13,family=By),node=E(pad=22,thickness=18,line=E(color=Bz,width=.5),label=FV,color=Im,x=Dr,y=Iw),link=E(source=CE,target=CF,value=CG,color=CH)));Ix.update_layout(title=f"💎 Combined Money Flow — {F} (Financing → Assets / Revenue, merged)",template=u,height=560,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ix,use_container_width=B,key=f"sankey_merged_{F}");A.caption("All money-related flows merged into one chart: financing sources (Equity + Reserves + Debt + Trade Payables) feed Total Financing, which splits into two parallel paths — Total Assets (incl. Trade Receivables) and Net Sales → Net Profit / Total Expenses. It's drawn as two branches off one hub, rather than one long chain, because Total Assets and Net Sales are different kinds of totals (balance sheet vs. P&L) that don't feed into each other. Trade Payables now also appears in the 🏗️ Capital Structure chart above.")
					else:A.info('Not enough financing / assets / revenue data available for this stock to build the Combined Money Flow chart.')
	A.markdown(c);A.subheader('📊 National Live Market Analytics Portal Framework');Z=A.tabs(['🔥 Most Active','🚀 Volume Gainers','🏆 Top Gainers/Losers','⭐ 52W Boundaries','📦 Stocks Traded','⚖️ Advances/Declines','🕒 Pre-Open Market','⚡ Price Band Hitters','🗺️ Index Ticker Heatmap','🎫 IPO Tracker','⚠️ Volume Shockers','📂 Document Reports','🖋️ TV Script Engine','🔮 MunafaSutra Tickers','🎯 Dhan Asset Registry','💎 Weekly Activity Metrics','🔧 ScanX Core Screener','🚦 ScanX Live Engine','🎨 Screener Exploration','📈 IPO Chittorgarh','🏷️ IPO Watch Panel','💓 NSE Pulse','📊 Chartink Screeners','📋 Chartink Dashboard','🗾 Chartink Atlas','📚 Mahesh Kaushik','💰 EFTI Wealth','✅ Securities Available','🏛️ Corporate Filings','📉 52W Low Market'])
	def a(url,label='Open in Browser'):return f"<div style='margin-bottom:8px;'><a href='{url}' target='_blank' style='display:inline-block; background:#1976d2; color:#fff; font-size:14px; font-weight:600;padding:8px 18px; border-radius:6px; text-decoration:none;'>🌐 {label}</a><span style='font-size:12px; color:#888; margin-left:12px;'>📱 Mobile: tap button if frame is blank</span></div>"
	with Z[0]:I='https://www.nseindia.com/market-data/most-active-equities';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[1]:I='https://www.nseindia.com/market-data/volume-gainers-spurts';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[2]:I='https://www.nseindia.com/market-data/top-gainers-losers';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[3]:I='https://www.nseindia.com/market-data/52-week-high-equity-market';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[4]:I='https://www.nseindia.com/market-data/stocks-traded';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[5]:I='https://www.nseindia.com/market-data/advance';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[6]:I='https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[7]:I='https://www.nseindia.com/market-data/upper-band-hitters';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[8]:I='https://www.nseindia.com/index-tracker/NIFTY%2050';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[9]:I='https://www.nseindia.com/market-data/all-upcoming-issues-ipo';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[10]:I='https://www.moneycontrol.com/stocks/market-stats/volume-shockers-nse/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[11]:I='https://www.nseindia.com/all-reports/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[12]:I='https://www.tradingview.com/scripts/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[13]:I='https://munafasutra.com/nse/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[14]:I='https://dhan.co/all-stocks-list/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[15]:I='https://dhan.co/stocks/market/most-active-stocks-this-week/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[16]:I='https://scanx.trade/create-custom-screener';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[17]:I='https://scanx.trade/stock-screener/live-market-screener';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[18]:I='https://www.screener.in/explore/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[19]:I='https://www.chittorgarh.com/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[20]:I='https://ipowatch.in/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[21]:I='https://nsepulse.streamlit.app/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[22]:I='https://chartink.com/screeners';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[23]:I='https://chartink.com/scan_dashboard';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[24]:I='https://chartink.com/atlas';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[25]:I='https://www.maheshkaushik.com/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[26]:I='https://eftiwealth.com/';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[27]:I='https://www.nseindia.com/static/market-data/securities-available-for-trading';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[28]:I='https://www.nseindia.com/companies-listing/corporate-filings-announcements';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[29]:I='https://www.nseindia.com/market-data/52-week-low-equity-market';A.markdown(a(I),unsafe_allow_html=B);Q.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	@DN
	def O4():
		z='Worst -> Best';y='1 Day';e='RANK';d='📊 BF Grade';b='🔬 BF Score';a='CURRENT PRICE';W='STOCK NAME';A.markdown(c);A.markdown('### 📈 Multi-Horizon Performance Summary Matrix');A0,AP=A.columns([4,1])
		with A0:f=A.radio(GJ,[GK,Cc,Cd],horizontal=B,help=KZ,key='perf_matrix_sizing_mode')
		g=[y,'2 Day','3 Day','5 Day','7 Day','10 Day','12 Day','15 Days','20 Days','25 Days',Go,'2 Months','3 Months','4 Months','5 Months','6 Months','7 Months','8 Months','9 Months','10 Months','11 Months',Gp,'18 Months','1.5 Years','2 Years','2.5 Years','3 Years',s];A1,A2,A3=A.columns([2,2,3])
		with A1:h=A.selectbox('🎯 Base Horizon for Performance Ranking:',g,index=0)
		with A2:A4=A.radio('排序 Sorting Order Type:',['Best -> Worst',z],index=0,horizontal=B)
		with A3:j=A.text_input('🔍 Filter stocks inside this matrix...',placeholder=J_,key=Ja)
		V={}
		for L in g:
			if L==s:
				if Aj:V[L]=Aj
				continue
			k=[L.lower(),L.lower().replace(' ',C),L.lower().replace('s',C)]
			if L==y:k.append(CV)
			for X in O:
				if Aa(A in X.lower()for A in k)and t in X.lower():V[L]=X;break
		if V:
			m=[]
			for(AQ,N)in K.iterrows():
				n=G(N.get(o,C)).strip();A5=N.get(q,C)if q else C;A6=f"https://charting.nseindia.com/?symbol={n}-EQ";A7=f'<a href="{A6}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{n}</a>';F={W:A7,a:A5}
				for(L,A9)in V.items():
					p=G(N.get(A9,'0')).replace(t,C).replace(AE,C).strip()
					try:F[L]=M(p)if p not in[C,A8,AR]else i
					except AZ:F[L]=i
				if AW:
					r=G(N.get(AW,'0')).replace(t,C).replace(AE,C).strip()
					try:F[Ao]=M(r)if r not in[C,A8,AR]else i
					except AZ:F[Ao]=i
				if BT:
					u=G(N.get(BT,C)).replace(t,C).replace(AE,C).strip()
					try:F[BP]=M(u)if u not in[C,A8,AR]else D
					except AZ:F[BP]=D
				if BW:
					v=G(N.get(BW,C)).replace(t,C).replace(AE,C).strip()
					try:F[B7]=M(v)if v not in[C,A8,AR]else D
					except AZ:F[B7]=D
				if AL:
					w=G(N.get(AL,C)).replace(AE,C).strip()
					try:F[Ap]=M(w)if w not in[C,A8,AR]else D
					except AZ:F[Ap]=D
				if AM:
					x=G(N.get(AM,C)).replace(AE,C).strip()
					try:F[Aq]=M(x)if x not in[C,A8,AR]else D
					except AZ:F[Aq]=D
				if Cl:F[Bs]=G(N.get(Cl,C)).strip()
				if BU:F[Bt]=G(N.get(BU,C)).strip()
				if DX:F[Bu]=G(N.get(DX,C)).strip()
				if DY:F[Bv]=G(N.get(DY,C)).strip()
				if BV:F[Bw]=G(N.get(BV,C)).strip()
				AA={A:B for(A,B)in N.items()if not G(A).startswith(Br)};AB,AC,_=DQ(AA,O);F[b]=AB;F[d]=AC;m.append(F)
			Q=H.DataFrame(m)
			if j:Q=Q[Q[W].str.replace(E0,C,regex=B).str.contains(j,case=J,na=J)]
			AF=h if h in Q.columns else Q.columns[2];AG=A4==z;Q=Q.sort_values(by=AF,ascending=AG).reset_index(drop=B);Q.insert(0,e,Q.index+1);E=Q.copy()
			for L in V.keys():
				if L in E.columns:
					if L==s:E[L]=E[L].apply(lambda x:f"{U(x):,}"if H.notnull(x)else l)
					else:E[L]=E[L].apply(lambda x:f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else'0.00%')
			if Ao in E.columns:E[Ao]=E[Ao].apply(lambda x:f"{x:.2f}%"if H.notnull(x)else l)
			if BP in E.columns:E[BP]=E[BP].apply(lambda x:f"{x:.2f}"if H.notnull(x)else l)
			if B7 in E.columns:E[B7]=E[B7].apply(lambda x:(f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else'0.00%')if H.notnull(x)else l)
			if Ap in E.columns:E[Ap]=E[Ap].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else l)
			if Aq in E.columns:E[Aq]=E[Aq].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else l)
			P=Ea.from_dataframe(E);P.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);P.configure_column(e,width=70,pinned=DH);P.configure_column(W,width=140,pinned=DH,cellRenderer=Dc);AH=B8('\n            function(params) {\n                if (params.value === undefined || params.value === null || params.colDef.field === "Volume") return null;\n                let val = parseFloat(String(params.value).replace(/[+%,]/g, \'\'));\n                if (val > 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#e6f4ea\', \'fontWeight\': \'bold\' };\n                if (val < 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#fce8e6\', \'fontWeight\': \'bold\' };\n                return null;\n            }\n            ');AI=B8(Ka);AJ=B8("\n            function(params) {\n                let v = String(params.value);\n                if (v.includes('STRONG BUY')) return { 'backgroundColor': '#16e37f44', 'fontWeight': 'bold' };\n                if (v.includes('WATCHLIST')) return { 'backgroundColor': '#f4b40044', 'fontWeight': 'bold' };\n                if (v.includes('CAUTION')) return { 'backgroundColor': '#ff990044' };\n                return { 'backgroundColor': '#ea433544' };\n            }\n            ");AK=B8(Kb)
			for I in E.columns:
				if I in(e,):continue
				if f==Cc and S(E)>0:Y=C0(E.iloc[0][I]);Z=S(G(I));R=U(AD(Y,Z)*7+22)
				elif f==Cd and S(E)>1:Y=C0(E.iloc[1][I]);Z=S(G(I));R=U(AD(Y,Z)*7+22)
				else:AN={W:140,a:130,Ao:110,b:110,d:160,BP:100,B7:140,Ap:110,Aq:110,Bs:120,Bt:130,Bu:130,Bv:130,Bw:130};R=AN.get(I,130)
				T=AD(70,min(R,90))
				if I==W:P.configure_column(I,width=R,minWidth=T,pinned=DH,cellRenderer=Dc)
				elif I==a:P.configure_column(I,width=R,minWidth=T)
				elif I==b:P.configure_column(I,width=R,minWidth=T,cellStyle=AI)
				elif I==d:P.configure_column(I,width=R,minWidth=T,cellStyle=AJ)
				elif I in(Bs,Bt,Bu,Bv,Bw):P.configure_column(I,width=R,minWidth=T,cellStyle=AK)
				elif I in V or I==B7:P.configure_column(I,width=R,minWidth=T,cellStyle=AH)
				else:P.configure_column(I,width=R,minWidth=T)
			P.configure_grid_options(domLayout=AT,rowHeight=38,headerHeight=45,enableCellTextSelection=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AO=P.build();EZ(E,gridOptions=AO,theme=GL,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=450,width=GM,key='horizon_perf_grid')
	O4()
	@DN
	def O5():
		m='Key Reasons';k='Score (High→Low)';W='Score';A.markdown(c);A.markdown('### 🔬 Bottom Fishing Scanner — Buy from Bottom Candidates');A.caption('Stocks that are 8–15% above 52W Low, in uptrend, with high volume + strong fundamentals');n,AI=A.columns([4,1])
		with n:a=A.radio(GJ,[GK,Cc,Cd],horizontal=B,help=KZ,key='bf_scanner_sizing_mode')
		p,r,s=A.columns([2,2,2])
		with p:X=A.slider('Minimum BF Score:',min_value=0,max_value=100,value=55,step=5,key='bf_min_score')
		with r:u=A.radio('Sort by:',[k,'Score (Low→High)'],horizontal=B,key='bf_sort')
		with s:b=A.text_input(Jz,placeholder='e.g. WIPRO',key=Jb)
		L=[]
		for(AJ,d)in K.iterrows():
			E={A:B for(A,B)in d.items()if not G(A).startswith(Br)};e,v,w=DQ(E,O)
			if e>=X:
				f=G(d.get(o,C)).strip();x=E.get(q,C)if q else C;g=R((A for A in O if EB in A.lower()),D);y=E.get(g,C)if g else C;z=f"https://charting.nseindia.com/?symbol={f}-EQ";A0=f'<a href="{z}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{f}</a>';Q=D
				if AW:
					h=G(E.get(AW,C)).replace(t,C).replace(AE,C).strip()
					try:Q=M(h)if h not in[C,A8,AR]else D
					except AZ:Q=D
				A1=G(E.get(BT,C)).strip()if BT else l;A2=G(E.get(BW,C)).strip()if BW else l;A3=G(E.get(AL,C)).strip()if AL else l;A4=G(E.get(AM,C)).strip()if AM else l;A5=G(E.get(Cl,C)).strip()if Cl else l;A6=G(E.get(BU,C)).strip()if BU else l;A7=G(E.get(DX,C)).strip()if DX else l;A9=G(E.get(DY,C)).strip()if DY else l;AA=G(E.get(BV,C)).strip()if BV else l;L.append({j:A0,W:e,GS:v,AP:x,BP:A1,Ao:f"{Q:.2f}%"if Q is not D else l,B7:A2,Ap:A3,Aq:A4,Bs:A5,Bt:A6,Bu:A7,Bv:A9,Bw:AA,Gb:G(y)[:30],m:' | '.join(w[:3])})
		if b:L=[A for A in L if b.upper()in re.sub(E0,C,A[j]).upper()]
		L.sort(key=lambda x:x[W],reverse=u==k)
		if L:
			A.success(f"✅ Found **{S(L)}** stocks matching your bottom-fishing criteria (score ≥ {X})");I=H.DataFrame(L);N=Ea.from_dataframe(I);N.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);AB=B8(Ka);AC=B8(Kb);AF={j:120,W:90,GS:160,AP:100,Ao:110,Gb:200,m:400,BP:100,B7:140,Ap:110,Aq:110,Bs:120,Bt:130,Bu:130,Bv:130,Bw:130}
			for F in I.columns:
				if a==Cc and S(I)>0:Y=C0(I.iloc[0][F]);Z=S(G(F));P=U(AD(Y,Z)*7+22)
				elif a==Cd and S(I)>1:Y=C0(I.iloc[1][F]);Z=S(G(F));P=U(AD(Y,Z)*7+22)
				else:P=AF.get(F,120)
				T=DH if F==j else D;V=AD(70,min(P,90))
				if F==W:N.configure_column(F,width=P,minWidth=V,pinned=T,cellStyle=AB)
				elif F==j:N.configure_column(F,width=P,minWidth=V,pinned=T,cellRenderer=Dc)
				elif F in(Bs,Bt,Bu,Bv,Bw):N.configure_column(F,width=P,minWidth=V,pinned=T,cellStyle=AC)
				else:N.configure_column(F,width=P,minWidth=V,pinned=T)
			N.configure_grid_options(domLayout=AT,rowHeight=40,headerHeight=45,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AG=N.build();EZ(I,gridOptions=AG,theme=GL,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=400,width=GM,key='bf_scanner_grid');i=io.BytesIO()
			with H.ExcelWriter(i,engine=DD)as AH:H0(I).to_excel(AH,index=J,sheet_name='Bottom Fishing')
			A.download_button('📥 Download BF Scanner Results',data=i.getvalue(),file_name=f"BottomFishing_{H.Timestamp.now().strftime(Bn)}.xlsx",mime=Bo)
		else:A.info(f"No stocks found with BF Score ≥ {X}. Try lowering the minimum score.")
	O5()
	if A1:
		A.markdown(c);A.markdown('### 🏆 Top 10 & Bottom 10 Performers (Daily badges)');CJ=K.copy();CJ[A1]=H.to_numeric(CJ[A1].astype(G).str.replace(BK,C,regex=B),errors=AQ);CJ=CJ.dropna(subset=[A1]);O6=CJ.nlargest(10,A1);O7=CJ.nsmallest(10,A1);Ax,Ay=A.columns(2)
		with Ax:
			Iy="<h4 style='margin-top:0px; margin-bottom:8px;'>⬆️ Top 10 (Daily)</h4>"
			for(_,Bh)in O6.iterrows():
				Cx=G(Bh.get(o,C)).strip();AI=Bh[A1];Cy=Bh.get(q,C)if q else C
				try:Bi=M(G(Cy).replace(AE,C).strip());Fb=M(AI);Fc=Bi/(1+Fb/100);Fd=Bi-Fc;Cz=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>+{Fd:,.2f}</span>";C_=f"₹{Bi:,.2f}"
				except:C_=f"₹{Cy}";Cz=C
				Fe=f"https://charting.nseindia.com/?symbol={Cx}-EQ";Iy+=f"<a href='{Fe}' target='_blank' style='text-decoration:none;'><div style='background-color:#16e37f; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cx}: +{AI}%</span><span>{Cz}{C_}</span></div></a>"
			A.markdown(Iy,unsafe_allow_html=B)
		with Ay:
			Iz="<h4 style='margin-top:0px; margin-bottom:8px;'>⬇️ Bottom 10 (Daily)</h4>"
			for(_,Bh)in O7.iterrows():
				Cx=G(Bh.get(o,C)).strip();AI=Bh[A1];Cy=Bh.get(q,C)if q else C
				try:Bi=M(G(Cy).replace(AE,C).strip());Fb=M(AI);Fc=Bi/(1+Fb/100);Fd=Bi-Fc;Cz=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>{Fd:,.2f}</span>";C_=f"₹{Bi:,.2f}"
				except:C_=f"₹{Cy}";Cz=C
				Fe=f"https://charting.nseindia.com/?symbol={Cx}-EQ";Iz+=f"<a href='{Fe}' target='_blank' style='text-decoration:none;'><div style='background-color:#f39991; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cx}: {AI}%</span><span>{Cz}{C_}</span></div></a>"
			A.markdown(Iz,unsafe_allow_html=B)
	A.markdown(c);A.markdown('### 📰 Global Market News, Alerts & Corporate Announcements');import urllib.request,urllib.parse,xml.etree.ElementTree as C6,pandas as H
	def Du(pubdate_str):
		try:
			D=H.to_datetime(pubdate_str,utc=B);G=H.Timestamp.now(tz=BQ);A=(G-D).total_seconds()
			if A<0:return AJ
			if A<60:return f"{U(A)} secs ago"
			if A<3600:E=U(A/60);return f"{E} min{"s"if E!=1 else C} ago"
			if A<86400:F=U(A/3600);return f"{F} hour{"s"if F!=1 else C} ago"
			if A<172800:return f"Yesterday ({D.strftime(EI)})"
			I=U(A/86400);return f"{I} days ago ({D.strftime(EI)})"
		except g:return GT
	@A.cache_data(ttl=600)
	def O8(symbol,limit=10):
		try:
			J=f'"{symbol}" NSE AND ("52 week high" OR "52 week low" OR "upper circuit" OR "lower circuit")';K=urllib.parse.quote(J);M=f"https://news.google.com/rss/search?q={K}&hl=en-IN&gl=IN&ceid=IN:en";N=urllib.request.Request(M,headers={Ce:Cf})
			with urllib.request.urlopen(N)as O:P=O.read()
			Q=C6.fromstring(P);R=[DB,EJ,CX,EK,EL,EM,EN,EO];E=[]
			for A in Q.findall(DK):
				F=A.find(A9).text
				if not Aa(A in F.lower()for A in R):continue
				S=A.find(f).text;I=A.find(At).text if A.find(At)is not D else C
				try:G=H.to_datetime(I,utc=B)
				except g:G=H.Timestamp.now(tz=BQ)-H.Timedelta(days=100)
				T=H.Timestamp.now(tz=BQ);U=(T-G).total_seconds()/86400
				if U<=15.:V=Du(I);E.append({AF:f"🚨 **[ALERT]** {F}",f:S,L:V,AK:G,Kc:F})
			E.sort(key=lambda x:x[AK],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def O9(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={Ce:Cf})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C6.fromstring(O);E=[];Q=[DB,EJ,CX,EK,EL,EM,EN,EO,Kd,Ke]
			for A in P.findall(DK):
				G=A.find(A9).text;R=A.find(f).text;I=A.find(At).text if A.find(At)is not D else C;S=Aa(A in G.lower()for A in Q);T=GU if S else C;U=f"{T}{G}"
				try:F=H.to_datetime(I,utc=B)
				except g:F=H.Timestamp.now(tz=BQ)-H.Timedelta(days=100)
				V=H.Timestamp.now(tz=BQ);W=(V-F).total_seconds()/86400
				if W<=Ar:X=Du(I);E.append({AF:U,f:R,L:X,AK:F})
			E.sort(key=lambda x:x[AK],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OA(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={Ce:Cf})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C6.fromstring(O);E=[];Q=[DB,EJ,CX,EK,EL,EM,EN,EO,Kd,Ke]
			for A in P.findall(DK):
				F=A.find(A9).text;R=A.find(f).text;G=A.find(At).text if A.find(At)is not D else C;S=Aa(A in F.lower()for A in Q);T=GU if S else C;U=f"{T}{F}"
				try:I=H.to_datetime(G,utc=B)
				except g:I=H.Timestamp.now(tz=BQ)-H.Timedelta(days=100)
				V=Du(G);E.append({AF:U,f:R,L:V,AK:I})
			E.sort(key=lambda x:x[AK],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OB(symbol,limit=6):
		try:
			I=f'"{symbol}" AND ("Regulation 30" OR "LODR" OR "Board Meeting" OR "AGM" OR "Analyst Meet" OR "Financial Results" OR "Corporate Action" OR "Dividend")';J=urllib.parse.quote(I);K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={Ce:Cf})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C6.fromstring(O);E=[]
			for A in P.findall(DK):
				Q=A.find(A9).text;R=A.find(f).text;F=A.find(At).text if A.find(At)is not D else C
				try:G=H.to_datetime(F,utc=B)
				except g:G=H.Timestamp.now(tz=BQ)-H.Timedelta(days=100)
				S=Du(F);E.append({AF:f"📢 {Q}",f:R,L:S,AK:G})
			E.sort(key=lambda x:x[AK],reverse=B);return E[:limit]
		except g:return[]
	OC={'RELIANCE':'500325','TCS':'532540','HDFCBANK':'500180','INFY':Ki,'ICICIBANK':'532174','HINDUNILVR':'500696','SBIN':'500112','BHARTIARTL':'532454','BAJFINANCE':'500034','KOTAKBANK':'500247','LT':'500510','HCLTECH':'532281','AXISBANK':'532215','ASIANPAINT':'500820','MARUTI':'532500',Kf:Kj,'TITAN':'500114','ULTRACEMCO':'532538','ONGC':'500312','NTPC':'532555','POWERGRID':'532898','WIPRO':'507685','NESTLEIND':'500790','JSWSTEEL':'500228','TATASTEEL':'500470','TATAMOTORS':'500570','TECHM':'532755','GRASIM':'500300','ADANIENT':'512599','ADANIPORTS':'532921','COALINDIA':'533278','DIVISLAB':Kk,'DRREDDY':'500124','EICHERMOT':'505200','BAJAJFINSV':'532978','BAJAJ-AUTO':'532977','CIPLA':'500087','BRITANNIA':'500825','HEROMOTOCO':'500182',Kg:Kl,'HINDALCO':'500440','UPL':'512070','TATACONSUM':'500800','SBILIFE':'540719','HDFCLIFE':'540777','INDUSINDBK':'532187','BPCL':'500547','IOC':'530965','M&M':'500520','PIDILITIND':'500331','SIEMENS':'500550','HAVELLS':'517354','VOLTAS':'500575','AMBUJACEM':'500425','ACC':'500410','SHREECEM':'500387','RAMCOCEM':Km,Kh:Kn,'JKCEMENT':'532644','STAR':Ko,'TVSMOTOR':'532343','BOSCHLTD':'500530','MUTHOOTFIN':'533398','CHOLAFIN':'500443','BAJAJHLDNG':'500490','TORNTPHARM':Kp,'AUROPHARMA':'524208','LUPIN':'500257','BIOCON':'532523','ALKEM':'539523','IPCALAB':'530827','GLAXO':'500660','ABBOTINDIA':'500488','PFIZER':'500680','SANOFI':'500674','MCDOWELL-N':'532432','ITC':'500875','GODFRYPHLP':'500163','COLPAL':'500830','DABUR':'500096','MARICO':'531642','GODREJCP':'532424','HINDPETRO':'500104','CASTROLIND':'500870','INDIGO':'521737','INTERGLOBE':'539448','SPICEJET':'500285','IRCTC':'542830','CONCOR':'531344','ADANIGREEN':'541450','ADANITRANS':'539254','TATAPOWER':'500400','TORNTPOWER':'532779','CESC':'500084','NHPC':'533098','SJVN':'533206','PFC':'532810','RECLTD':'532955','IRFC':'543257','ZOMATO':'543320','NYKAA':'543384','PAYTM':'543396','POLICYBZR':'543390','DELHIVERY':'543529','CARTRADE':'543202','RVNL':'542649','IRCON':'541956','NBCC':'534309','HUDCO':'540530','MMTC':Kq,'MTNL':'500108','BEL':'500049','HAL':'541154','COCHINSHIP':'526235','MAZAGON':'543237','GRSE':'542351','MIDHANI':'541195','BEML':'500048','BHEL':'500103','SAIL':'500113','NMDC':'526371','MOIL':'533286','NATIONALUM':'532234','HINDZINC':'500188','VEDL':'500295','GMRINFRA':'532754','NHAI':'500253','IRB':'532947','ASHOKLEY':'500477','ESCORTS':'500495','FORCE':'517168','SML':'513275','MOTHERSON':'517334','MINDAIND':'532539','ENDURANCE':'540350','BALKRISIND':'502355','APOLLOTYRE':'500877','MRF':'500290','CEATLTD':'500878','JK TYRE':'530007','INOXWIND':'539083','SUZLON':'532667','RPOWER':'500390','JPPOWER':'532627','FEDERALBNK':'500469','IDFCFIRSTB':'539437','BANDHANBNK':'541153','RBLBANK':'540065','DCBBANK':'532772','KTKBANK':Kr,'SOUTHBANK':'532218','CANBK':'532483','BANKBARODA':'532134','UNIONBANK':'532477','INDIANB':'532814','UCOBANK':'532505','CENTRALBK':'532885','MAHABANK':'532525','J&KBANK':Kr,'PNB':'532461','IOB':'532388','BANKINDIA':'532149','DENABANK':'532121','SYNDIBANK':'532276','VIJAYABANK':'532245','ORIENTBANK':'500315','CORPBANK':'532179','ANDHRABANK':'532418','ALLAHABAD':Ks,'ALBK':Ks,'MFSL':'542299','HDFCAMC':'541530','NIPPONLIFE':'543171','UTIAMC':'543238','ABCAPITAL':'540691','ANGELONE':'543235','ICICIGI':'540716','GICRE':'540755','NIACL':'540769','STAR':Ko,'CROMPTON':'539876','ORIENTELEC':'531637','BLUESTAR':'500067','WHIRLPOOL':'500238','VGUARD':'532953','BAJAJEL':'500031','CERA':'532443','HINDWARE':'509820','HSIL':'509675','KAJARIACER':'500233','SOMANYCER':'532622','GRINDWELL':'506076','CARBORUNIV':'513375','ASTRAL':'532830','FINOLEX':'500940','SUPREMEIND':'509930','BERGER':'509480','KANSAINER':'500165','AKZOINDIA':'500710','INDIACEM':'530005','RAMCOIND':Km,Kh:Kn,'HEIDELBERG':'500292','PRISM':'500338','BIRLACORPN':'500335','ORIENTCEM':'502420','SAGCEM':'502090','STARCEMENT':'540575','JKLAKSHMI':'500380','NUVOCO':'543334','ZYDUSLIFE':'532321','TORNTPHAR':Kp,'NATCOPHAR':'524816','GRANULES':'532482','LAURUS':Kt,'STRIDES':'532531','AJANTPHAR':'532331','CAPLIPOINT':'539266','DIVI':Kk,Kf:Kj,'GLAND':'543245','SEQUENT':'543225','METROPOLIS':'542650','DRLAL':'532259','THYROCARE':'539871','KRSNAA':'543328','VIJAYA':'532542','MAXHEALTH':'543220','KIMS':'543308','ASTER':'540975','FORTIS':'532843','NHOSPIT':'532526',Kg:Kl,'NARAYANA':'539551','YATHARTH':'544120','RAINBOW':'543524','SUVENPHAR':'530239','LAURUSLABS':Kt,'SOLARA':'541540','SHILPAMED':'530879','PERSISTENT':'533179','MINDTREE':'532819','MPHASIS':'526299','HEXAWARE':'532861','NIIT':'500304','KPIT':'542651','LTTS':'540115','COFORGE':'532541','ZENSAR':'504067','RAMSYSTEMS':'532370','MASTEK':'523704','SASKEN':'532663','TATAELXSI':'500408','CYIENT':'532175','SONATSOFTW':'532221','TANLA':'532790','LTIM':'540005','INFY':Ki,'ROUTE':'543228','BSOFT':'526301','NEWGEN':'540900','INTELLECT':'538835','NUCLEUS':'531209','NELCO':'504112','DELTACORP':'532840','WONDERLA':'538268','MAHINDCIE':'532756','STARHLTH':'543412','NAUKRI':'532777','JUSTDIAL':'535648','MATRIMONY':'539846','MAKEMYTRIP':Kq,'IXIGO':'544229','RATEGAIN':'543417','TEAMLEASE':'539658','QUESS':'539978','SIS':'540673','SECURKLOUD':'539963','HAPPYFORGE':'543532','KALYANKJIL':'543278','SENCO':'543456','THANGAMAYL':'531509','TRIBHOVAND':'512415','PC JEWELLER':'534809','RAJESHEXPO':'531500'}
	@A.cache_data(ttl=600)
	def OD(bse_code,days_back=90):
		L='SUBCATNAME';A={Gq:[],Gr:[],Gs:[],Gt:[],EW:[]}
		try:
			import datetime as F;G=F.date.today();M=G-F.timedelta(days=days_back);N=M.strftime(Bn);O=G.strftime(Bn);P=f"https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w?pageno=1&strCat=-1&strPrevDate={N}&strScrip={bse_code}&strSearch=P&strToDate={O}&strType=C&subcategory=-1";Q={Ce:Cf,'Referer':'https://www.bseindia.com/','Accept':'application/json'};R=urllib.request.Request(P,headers=Q)
			with urllib.request.urlopen(R,timeout=8)as S:T=EY.loads(S.read())
			for B in(T.get('Table')or[])[:30]:
				U=B.get('HEADLINE',C)or B.get(L,C);I=B.get('NEWS_DT',C)or B.get('DT_TM',C);J=B.get('NEWSID',C);V=f"https://www.bseindia.com/xml-data/corpfiling/AttachLive/{J}.pdf"if J else C
				try:K=H.to_datetime(I).strftime(EI)
				except g:K=I[:10]
				E=(B.get(L)or C).lower();D={A9:U,f:V,As:K}
				if Aa(A in E for A in['annual report','annual rep']):A[Gr].append(D)
				elif Aa(A in E for A in['credit rat','rating']):A[Gs].append(D)
				elif Aa(A in E for A in['concall','con call','earnings call','analyst']):A[Gt].append(D)
				elif Aa(A in E for A in['investor presentation','presentation',EW]):A[EW].append(D)
				else:A[Gq].append(D)
		except g:pass
		return A
try:
	CK=K[o].dropna().unique()
	if S(CK)>0:
		OE,OF,OG,OH,OI,OJ,OK=A.tabs(['🚨 Latest Alerts Timeline','🏢 Alerts by Stock','📰 Smart News Engine (1 Day)','📰 Smart News Engine (All News)','📢 Corporate Announcements','📢 DOCUMENTS HUB','📜 Rules']);D0=[];I_=CK[:30]
		with A.spinner('Scanning Top 30 stocks for Circuit & 52-Week Breakouts (15 Days)...'):
			for F in I_:
				A6=G(F).strip();BF=O8(A6,limit=15)
				for B1 in BF:B1[Ad]=A6;D0.append(B1)
		OL={A[Ad]for A in D0};J0={A[Ad]for A in D0 if Af in A[L]or Ag in A[L]or Ah in A[L]or AJ in A[L]}
		def OM(sym):
			A=sym
			if A in J0:B,C,D=Ae,'#003300','#0fbf62'
			elif A in OL:B,C,D='#1a7a45',D4,'#145e34'
			else:B,C,D='#444',D4,'#333'
			return f"<span style='background:{B}; color:{C}; padding:2px 9px; border-radius:5px; font-weight:700; font-size:0.82em; border:1px solid {D}; white-space:nowrap;'>⚡ {A}</span>"
		with OE:
			ON,OO,OP=A.columns([2,1,1]);J1=ON.text_input('🔍 Search Alerts:',placeholder='e.g. ICICIBANK, circuit...',key='global_news_search');J2=OO.selectbox('⏳ Time Filter:',['All (Up to 15 Days)',Ku,Kv],key='global_news_time');OQ=OP.radio('↕️ Sort By Time:',[Kw,'Oldest First'],horizontal=B,key='global_news_sort');B2=D0.copy()
			if J1:J3=J1.lower();B2=[A for A in B2 if J3 in A[Ad].lower()or J3 in A[Kc].lower()]
			if J2==Kv:B2=[A for A in B2 if Af in A[L]or Ag in A[L]or Ah in A[L]or AJ in A[L]]
			elif J2==Ku:OR=H.Timestamp.now(tz=BQ);B2=[A for A in B2 if(OR-A[AK]).total_seconds()/86400<=7.]
			B2.sort(key=lambda x:x[AK],reverse=OQ==Kw);A.markdown(Cb,unsafe_allow_html=B)
			if B2:
				for N in B2:h=Af in N[L]or Ag in N[L]or Ah in N[L]or AJ in N[L];w=Ae if h else B6;x=AU if h else AT;OS=OM(N[Ad]);A.markdown(f"- {OS}&nbsp; <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.4em 0; opacity: 0.15;'>",unsafe_allow_html=B)
			else:A.info('No circuit or 52-week alerts match your search or filter criteria.')
		with OF:
			OT=A.columns(2);Ff=0
			for A6 in[G(A).strip()for A in I_]:
				Dv=[A for A in D0 if A[Ad]==A6];Dv.sort(key=lambda x:x[AK],reverse=B)
				if Dv:
					with OT[Ff%2]:
						OU='🟢'if A6 in J0 else'🟡'
						with A.expander(f"{OU} {A6} Action Alerts (0 Sec to 15 Days)",expanded=B):
							OV=Dv[:3];Fg=Dv[3:]
							for N in OV:h=Af in N[L]or Ag in N[L]or Ah in N[L]or AJ in N[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fg:
								with A.expander(f"🔽 Show {S(Fg)} more older alerts",expanded=J):
									for N in Fg:h=Af in N[L]or Ag in N[L]or Ah in N[L]or AJ in N[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Ff+=1
			if Ff==0:A.info('No circuit breakouts or 52-week boundary alerts for the currently filtered stocks in the last 15 days.')
		with OG:
			A.markdown('### Latest News & Action Alerts (Past 24 Hours)');OW=A.columns(2);Fh=0
			for D1 in CK[:10]:
				A6=G(D1).strip();BF=O9(A6,limit=5)
				if BF:
					with OW[Fh%2]:
						with A.expander(f"📰 {A6} News Feed (0 Sec to 1 Day)",expanded=B):
							for N in BF:h=Af in N[L]or Ag in N[L]or Ah in N[L]or AJ in N[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fh+=1
			if Fh==0:A.info('No general news found for the currently filtered stocks in the last 24 hours.')
		with OH:
			A.markdown('### Latest News & Action Alerts (All Time)');OX=A.columns(2);Fi=0
			for D1 in CK[:10]:
				A6=G(D1).strip();BF=OA(A6,limit=6)
				if BF:
					with OX[Fi%2]:
						with A.expander(f"📰 {A6} News Feed (All News)",expanded=B):
							OY=BF[:3];Fj=BF[3:]
							for N in OY:h=Af in N[L]or Ag in N[L]or Ah in N[L]or AJ in N[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fj:
								with A.expander(f"🔽 Show {S(Fj)} more articles",expanded=J):
									for N in Fj:h=Af in N[L]or Ag in N[L]or Ah in N[L]or AJ in N[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fi+=1
			if Fi==0:A.info('No general news found for the currently filtered stocks.')
		with OI:
			A.markdown('### 📢 Official Exchange Filings & Corporate Announcements');A.markdown("<span style='font-size: 0.9em; color: gray;'>Tracks Regulation 30, LODR, Board Meetings, AGMs, and Analyst Meets.</span>",unsafe_allow_html=B);A.markdown(Cb,unsafe_allow_html=B);OZ=A.columns(2);Fk=0
			for D1 in CK[:15]:
				A6=G(D1).strip();Fl=OB(A6,limit=7)
				if Fl:
					with OZ[Fk%2]:
						with A.expander(f"📢 {A6} Filings & Announcements",expanded=B):
							Oa=Fl[:3];Fm=Fl[3:]
							for A7 in Oa:h=Af in A7[L]or Ag in A7[L]or Ah in A7[L]or AJ in A7[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{A7[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A7[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {A7[L]}</span>",unsafe_allow_html=B)
							if Fm:
								with A.expander(f"🔽 Show {S(Fm)} more filings",expanded=J):
									for A7 in Fm:h=Af in A7[L]or Ag in A7[L]or Ah in A7[L]or AJ in A7[L];w=Ae if h else B6;x=AU if h else AT;A.markdown(f"- <a href='{A7[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A7[AF]}</a> <span style='color: {w}; font-weight: {x}; font-size: 0.85em;'>— 🕒 {A7[L]}</span>",unsafe_allow_html=B)
					Fk+=1
			if Fk==0:A.info('No recent corporate filings or official announcements found for the filtered stocks.')
		with OJ:
			A.markdown('### 📄 Documents Hub — Announcements · Annual Reports · Credit Ratings · Concalls · PPT · REC');A.markdown("<span style='font-size:0.88em; color:#888;'>Live BSE India filings (public API, no key needed). Annual Reports & Concalls also link to Screener.in.</span>",unsafe_allow_html=B);A.markdown(Cb,unsafe_allow_html=B);Ob,Oc,Od=A.columns([3,1.2,1.2])
			with Ob:J4=[G(A).strip()for A in CK[:60]];J5=A.multiselect('🔍 Stocks to view:',options=J4,default=J4[:4],key='doc_hub_stocks_v2')
			with Oc:Oe=A.selectbox('📅 Date range:',[Go,Kx,Ky,Gp],index=1,key='doc_days_v2')
			with Od:J6=A.selectbox('📋 Rows per section:',[3,5,8,12],index=1,key='doc_limit_v2')
			Of={Go:30,Kx:90,Ky:180,Gp:365};Og=Of[Oe]
			if not J5:A.info('Select at least one stock above to view its documents.')
			else:
				for p in J5:
					z=OC.get(p.upper(),C)
					with A.expander(f"📁  {p}   {"· BSE "+z if z else"· BSE code not mapped — Screener links shown"}",expanded=B):
						Fn="<div style='display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;'>";Oh=[('📢 BSE Announcements',f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={z}"if z else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={p}",Kz,K_),('📑 Annual Reports',f"https://www.screener.in/company/{p}/",Ca,L0),('⭐ Credit Ratings',f"https://www.screener.in/company/{p}/",GH,'#f57f17'),('🎙️ Concalls',f"https://www.screener.in/company/{p}/",'#fce4ec',DM),('📊 Investor PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={z}"if z else f"https://www.screener.in/company/{p}/",L1,L2),('🏛️ NSE Filings',f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={p}",'#e0f7fa','#00695c'),('📈 Screener',f"https://www.screener.in/company/{p}/",'#fffde7',B5)]
						for(Fo,Fp,Fq,Fr)in Oh:Fn+=f"<a href='{Fp}' target='_blank' style='background:{Fq}; color:{Fr}; padding:5px 12px; border-radius:6px; font-size:0.78em; font-weight:600; text-decoration:none; white-space:nowrap;'>{Fo}</a>"
						Fn+=D3;A.markdown(Fn,unsafe_allow_html=B);CL={}
						if z:
							with A.spinner(f"Fetching BSE filings for {p}…"):CL=OD(z,days_back=Og)
						Oi,Oj,Ok,Ol=A.columns([3,2,2,3])
						with Oi:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #5c6bc0; padding-bottom:4px; color:#5c6bc0;'>📢 Announcements</p>",unsafe_allow_html=B);J7=CL.get(Gq,[])
							if J7:
								Om,On=A.tabs([GT,'All ↗'])
								with Om:
									for CM in J7[:J6]:BG=CM[A9][:85]+'…'if S(CM[A9])>85 else CM[A9];Bj=f"<a href='{CM[f]}' target='_blank' style='color:#5c6bc0; text-decoration:none;'>{BG}</a>"if CM[f]else f"<span>{BG}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:6px; border-left:3px solid #c5cae9; padding-left:6px;'>{Bj}<br><span style='color:#aaa; font-size:0.85em;'>{CM[As]}</span></div>",unsafe_allow_html=B)
								with On:Oo=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={z}"if z else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={p}";A.markdown(f"<a href='{Oo}' target='_blank' style='color:#5c6bc0; font-size:0.85em;'>🔗 Open full announcements page →</a>",unsafe_allow_html=B)
							else:Op=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={z}"if z else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={p}";A.markdown(f"<a href='{Op}' target='_blank' style='color:#5c6bc0; font-size:0.83em;'>🔗 View on {"BSE"if z else"NSE"} →</a>",unsafe_allow_html=B);A.caption('No announcements in selected date range.')
						with Oj:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #43a047; padding-bottom:4px; color:#43a047;'>📑 Annual Reports</p>",unsafe_allow_html=B);J8=CL.get(Gr,[])
							if J8:
								for Dw in J8[:6]:J9=Dw[As][:4]if Dw[As]else'Report';Bj=f"<a href='{Dw[f]}' target='_blank' style='color:#43a047; text-decoration:none;'>📄 Annual Report {J9}</a>"if Dw[f]else f"<span>📄 Annual Report {J9}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px;'>{Bj}</div>",unsafe_allow_html=B)
							else:
								if z:A.markdown(f"<a href='https://www.bseindia.com/AnnualReports.html?scripcd={z}' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 BSE Annual Reports →</a>",unsafe_allow_html=B)
								A.markdown(f"<a href='https://www.screener.in/company/{p}/' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 View on Screener →</a>",unsafe_allow_html=B);A.caption('Not found in selected range — try 1 Year.')
						with Ok:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #f57f17; padding-bottom:4px; color:#f57f17;'>⭐ Credit Ratings</p>",unsafe_allow_html=B);JA=CL.get(Gs,[])
							if JA:
								for CN in JA[:4]:BG=CN[A9][:70]+'…'if S(CN[A9])>70 else CN[A9];Bj=f"<a href='{CN[f]}' target='_blank' style='color:#f57f17; text-decoration:none;'>{BG}</a>"if CN[f]else f"<span>{BG}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffe0b2; padding-left:6px;'>{Bj}<br><span style='color:#aaa; font-size:0.85em;'>{CN[As]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{p}/' target='_blank' style='color:#f57f17; font-size:0.83em;'>⭐ Ratings on Screener →</a>",unsafe_allow_html=B);A.markdown("<div style='font-size:0.78em; margin-top:8px; color:#888;'><a href='https://www.careratings.com' target='_blank' style='color:#888;'>CARE</a> · <a href='https://www.icra.in' target='_blank' style='color:#888;'>ICRA</a> · <a href='https://www.crisil.com' target='_blank' style='color:#888;'>CRISIL</a> · <a href='https://www.infomerics.com' target='_blank' style='color:#888;'>Infomerics</a></div>",unsafe_allow_html=B);A.caption('Not found via BSE — check links above.')
						with Ol:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #e53935; padding-bottom:4px; color:#e53935;'>🎙️ Concalls &amp; Investor Docs</p>",unsafe_allow_html=B);Oq=CL.get(Gt,[]);JB=CL.get(EW,[]);JC=JB+Oq
							if JC:
								for Bk in JC[:J6]:Or=Bk in JB;JD='📊'if Or else'🎙️';BG=Bk[A9][:70]+'…'if S(Bk[A9])>70 else Bk[A9];Bj=f"<a href='{Bk[f]}' target='_blank' style='color:#e53935; text-decoration:none;'>{JD} {BG}</a>"if Bk[f]else f"<span>{JD} {BG}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffcdd2; padding-left:6px;'>{Bj}<br><span style='color:#aaa; font-size:0.85em;'>{Bk[As]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{p}/' target='_blank' style='color:#e53935; font-size:0.83em;'>🎙️ Concalls on Screener →</a>",unsafe_allow_html=B);A.caption('No concalls/PPT in selected date range.')
							A.markdown(Cb,unsafe_allow_html=B);Fs="<div style='display:flex; gap:6px; flex-wrap:wrap;'>";Os=[('📝 Transcript',f"https://www.screener.in/company/{p}/",Kz,K_),('🤖 AI Summary',f"https://www.screener.in/company/{p}/",Ca,L0),('📊 PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={z}"if z else f"https://www.screener.in/company/{p}/",L1,L2),('▶️ REC',f"https://www.youtube.com/results?search_query={p}+concall+earnings",Bp,DE)]
							for(Fo,Fp,Fq,Fr)in Os:Fs+=f"<a href='{Fp}' target='_blank' style='background:{Fq}; color:{Fr}; padding:3px 10px; border-radius:4px; font-size:0.76em; font-weight:600; text-decoration:none;'>{Fo}</a>"
							Fs+=D3;A.markdown(Fs,unsafe_allow_html=B)
		with OK:A.markdown('### 📜 Trading Rules');A.markdown("<span style='font-size:0.88em; color:#888;'>Edit the <code>TRADING_RULES_LIBRARY</code> constant near the top of the .py file to change anything shown below — same pattern as the AI Prompt Library &amp; Pine Script Custom Rules Library.</span>",unsafe_allow_html=B);A.markdown(Cb,unsafe_allow_html=B);A.markdown(LA)
	else:A.info('No stocks currently filtered to check.')
except g as Bb:A.error(f"⚠️ Could not load the News Engine. Error details: {Bb}")
else:A.warning('No data loaded. Check sheet sharing and secrets.')
