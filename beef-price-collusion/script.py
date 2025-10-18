import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

beef_us = pd.read_csv('./data/raw/ground beef - us city.csv')
beans_us = pd.read_csv('./data/raw/beans - us city.csv')
cheese_us = pd.read_csv('./data/raw/cheese - us city.csv')
ice_cream_us = pd.read_csv('./data/raw/ice cream - us city.csv')
milk_us = pd.read_csv('./data/raw/milk - us city.csv')
food_cpi_us = pd.read_csv('./data/raw/food cpi - us.csv')
food_ppi_us = pd.read_csv('./data/raw/food ppi - us.csv')

beef_us = beef_us.rename(columns={'APU0000703112': 'avg price ground beef (US)'})
beans_us = beans_us.rename(columns={'APU0000714233': 'avg price dried beans (US)'})
cheese_us = cheese_us.rename(columns={'APU0000710212': 'avg price cheddar cheese (US)'})
ice_cream_us = ice_cream_us.rename(columns={'APU0000710411': 'avg price ice cream (US)'})
milk_us = milk_us.rename(columns={'APU0000709112': 'avg price milk (US)'})
food_cpi_us = food_cpi_us.rename(columns={'CPIUFDSL': 'food cpi (US)'})
food_ppi_us = food_ppi_us.rename(columns={'PCU311311': 'food ppi (US)'})

merged_beef_beans = pd.merge(beef_us, beans_us, on='observation_date', how='inner')
us_merged_price = pd.merge(merged_beef_beans, cheese_us, on='observation_date', how='inner')
us_merged_price = pd.merge(us_merged_price, milk_us, on='observation_date', how='inner')
us_merged_price = pd.merge(us_merged_price, ice_cream_us, on='observation_date', how='inner')
us_merged_price = pd.merge(us_merged_price, food_cpi_us, on='observation_date', how='inner')
us_merged_price = pd.merge(us_merged_price, food_ppi_us, on='observation_date', how='inner')

us_merged_price = us_merged_price[us_merged_price['observation_date'] >= '1996-01-01']

print(us_merged_price.head())

us_merged_price.to_csv('./data/derived/us_merged_price.csv', index=False)

us_merged_price['observation_date'] = pd.to_datetime(us_merged_price['observation_date'])
us_merged_price = us_merged_price.dropna()

plt.figure(figsize=(12, 6))
plt.plot(us_merged_price['observation_date'], us_merged_price['avg price ground beef (US)'], label='Ground Beef', color='indigo')
plt.plot(us_merged_price['observation_date'], us_merged_price['avg price dried beans (US)'], label='Dried Beans', color='mediumpurple')
plt.plot(us_merged_price['observation_date'], us_merged_price['avg price cheddar cheese (US)'], label='Cheddar Cheese', color='purple')
plt.plot(us_merged_price['observation_date'], us_merged_price['avg price ice cream (US)'], label='Ice Cream', color='hotpink')
plt.plot(us_merged_price['observation_date'], us_merged_price['avg price milk (US)'], label='Milk', color='lightpink')
plt.axvspan('2001-03-01', '2001-11-01', color='gray', alpha=0.5, label='Recession')
plt.axvspan('2007-12-01', '2009-06-01', color='gray', alpha=0.5)
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Average Price Per Pound (US$/lb)')
plt.title('Price Trends in the US (1996-Present)')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('./data/figures/us_price.png', format='png')
plt.show()

us_merged_price_zoom = us_merged_price[(us_merged_price['observation_date'] >= '1996-01-01') & 
                                      (us_merged_price['observation_date'] <= '2000-12-31')]

plt.figure(figsize=(12, 6))
plt.plot(us_merged_price_zoom['observation_date'], us_merged_price_zoom['avg price ground beef (US)'], label='Ground Beef', color='indigo')
plt.plot(us_merged_price_zoom['observation_date'], us_merged_price_zoom['avg price dried beans (US)'], label='Dried Beans', color='mediumpurple')
plt.axvline(pd.to_datetime('2000-01-01'), color='red', linestyle='--', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Average Price Per Pound (US$/lb)')
plt.title('Zoomed-In Price Trends (1996-2000)')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.xlim(pd.to_datetime('1996-01-01'), pd.to_datetime('2000-12-31'))
plt.xticks(rotation=45)
plt.savefig('./data/figures/zoom_us.png', format='png')
plt.show()

base_year = 2000
base_prices = us_merged_price[us_merged_price['observation_date'].dt.year == base_year]

base_beef_price = base_prices['avg price ground beef (US)'].iloc[0]
base_beans_price = base_prices['avg price dried beans (US)'].iloc[0]
base_cheese_price = base_prices['avg price cheddar cheese (US)'].iloc[0]

us_merged_price['beef_price_index'] = (us_merged_price['avg price ground beef (US)'] / base_beef_price) * 100
us_merged_price['beans_price_index'] = (us_merged_price['avg price dried beans (US)'] / base_beans_price) * 100
us_merged_price['cheese_price_index'] = (us_merged_price['avg price cheddar cheese (US)'] / base_cheese_price) * 100

plt.figure(figsize=(12, 6))
plt.plot(us_merged_price['observation_date'], us_merged_price['beef_price_index'], label='Ground Beef', color='indigo')
plt.plot(us_merged_price['observation_date'], us_merged_price['beans_price_index'], label='Dried Beans', color='mediumpurple')
plt.plot(us_merged_price['observation_date'], us_merged_price['cheese_price_index'], label='Cheddar Cheese', color='purple')
plt.axvspan('2001-03-01', '2001-11-01', color='gray', alpha=0.5, label='Recession')
plt.axvspan('2007-12-01', '2009-06-01', color='gray', alpha=0.5)
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Price Index (Base Year: 2000)')
plt.title('Subset of Indexed Price Trends in the US')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('./data/figures/indexed_trifecta.png', format='png')
plt.show()

base_ice_cream_price = base_prices['avg price ice cream (US)'].iloc[0]
base_milk_price = base_prices['avg price milk (US)'].iloc[0]

us_merged_price['ice_cream_price_index'] = (us_merged_price['avg price ice cream (US)'] / base_ice_cream_price) * 100
us_merged_price['milk_price_index'] = (us_merged_price['avg price milk (US)'] / base_milk_price) * 100

plt.figure(figsize=(12, 6))
plt.plot(us_merged_price['observation_date'], us_merged_price['beef_price_index'], label='Ground Beef', color='indigo')
plt.plot(us_merged_price['observation_date'], us_merged_price['beans_price_index'], label='Dried Beans', color='mediumpurple')
plt.plot(us_merged_price['observation_date'], us_merged_price['cheese_price_index'], label='Cheddar Cheese', color='deeppink')
plt.plot(us_merged_price['observation_date'], us_merged_price['ice_cream_price_index'], label='Ice Cream', color='hotpink')
plt.plot(us_merged_price['observation_date'], us_merged_price['milk_price_index'], label='Milk', color='lightpink')
plt.axvspan('2001-03-01', '2001-11-01', color='gray', alpha=0.5, label='Recession')
plt.axvspan('2007-12-01', '2009-06-01', color='gray', alpha=0.5)
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Price Index (Base Year: 2000)')
plt.title('Full Indexed Price Trends in the US')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('./data/figures/us_indexed_all.png', format='png')
plt.show()

base_food_cpi = base_prices['food cpi (US)'].iloc[0]
base_food_ppi = base_prices['food ppi (US)'].iloc[0]

us_merged_price['food_cpi_index'] = (us_merged_price['food cpi (US)'] / base_food_cpi) * 100
us_merged_price['food_ppi_index'] = (us_merged_price['food ppi (US)'] / base_food_ppi) * 100

plt.figure(figsize=(12, 6))

plt.plot(us_merged_price['observation_date'], us_merged_price['beef_price_index'], label='Ground Beef', color='indigo')
plt.plot(us_merged_price['observation_date'], us_merged_price['beans_price_index'], label='Dried Beans', color='mediumpurple')
plt.plot(us_merged_price['observation_date'], us_merged_price['cheese_price_index'], label='Cheddar Cheese', color='deeppink')
plt.plot(us_merged_price['observation_date'], us_merged_price['ice_cream_price_index'], label='Ice Cream', color='hotpink')
plt.plot(us_merged_price['observation_date'], us_merged_price['milk_price_index'], label='Milk', color='lightpink')
plt.plot(us_merged_price['observation_date'], us_merged_price['food_cpi_index'], label='Food (Consumers)', color='red', linestyle=':')
plt.plot(us_merged_price['observation_date'], us_merged_price['food_ppi_index'], label='Food (Producers)', color='orange', linestyle=':')
plt.axvspan('2001-03-01', '2001-11-01', color='gray', alpha=0.5, label='Recession')
plt.axvspan('2007-12-01', '2009-06-01', color='gray', alpha=0.5)
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Price Index (Base Year: 2000)')
plt.title('Comparative Indexed Price Trends in the US')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('./data/figures/us_indexed_final.png', format='png')
plt.show()

beef_ca = pd.read_csv('./data/raw/ground beef - ca.csv')

beef_ca = beef_ca.rename(columns={'REF_DATE': 'observation_date'})
beef_ca = beef_ca.rename(columns={'VALUE': 'avg price ground beef (CA)'})

beef_ca['observation_date'] = pd.to_datetime(beef_ca['observation_date'], format='%Y-%m')  

clean_beef_ca = beef_ca[['observation_date', 'avg price ground beef (CA)']]

print(clean_beef_ca.head())

us_merged_price = pd.merge(us_merged_price, clean_beef_ca, on='observation_date', how='inner')

us_merged_price.to_csv('./data/derived/us_merged_price.csv', index=False)

base_year = 2000
base_prices = us_merged_price[us_merged_price['observation_date'].dt.year == base_year]

base_beef_ca = base_prices['avg price ground beef (CA)'].iloc[0]
us_merged_price['beef_ca_index'] = (us_merged_price['avg price ground beef (CA)'] / base_beef_ca) * 100

us_merged_price.to_csv('./data/derived/us_merged_price.csv', index=False)

print(us_merged_price.head())

us_merged_price_zoom_index = us_merged_price[(us_merged_price['observation_date'] >= '1996-01-01') & 
                                      (us_merged_price['observation_date'] <= '2000-12-31')]

plt.figure(figsize=(12, 6))
plt.plot(us_merged_price_zoom_index['observation_date'], us_merged_price_zoom_index['beef_price_index'], label='U.S. Beef', color='#1f77b4')
plt.plot(us_merged_price_zoom_index['observation_date'], us_merged_price_zoom_index['beef_ca_index'], label='Canadian Beef', color='#ff7f0e')
plt.plot(us_merged_price_zoom_index['observation_date'], us_merged_price_zoom_index['beans_price_index'], label='U.S. Beans', color='#2ca02c')
plt.plot(us_merged_price_zoom_index['observation_date'], us_merged_price_zoom_index['cheese_price_index'], label='U.S. Cheese', color='#e377c2')
plt.plot(us_merged_price_zoom_index['observation_date'], us_merged_price_zoom_index['milk_price_index'], label='U.S. Milk', color='#9467bd')
plt.axvline(pd.to_datetime('2000-01-01'), color='red', linestyle='--', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('Zoomed-In Price Index Trends (1996-2000)')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.xlim(pd.to_datetime('1996-01-01'), pd.to_datetime('2000-12-31'))
plt.xticks(rotation=45)
plt.savefig('./data/figures/zoom_index.png', format='png')
plt.show()

food_ca = pd.read_csv('./data/raw/food - ca.csv')
food_ca = food_ca.rename(columns={'REF_DATE': 'observation_date'})
food_ca['observation_date'] = pd.to_datetime(food_ca['observation_date'], format='%Y-%m')  

rows = [
    "Milk, 4 litres", 
    "Dry beans and legumes, 900 grams ", 
]

clean_food_ca = food_ca[food_ca['Products'].isin(rows)]
clean_food_ca = clean_food_ca[['observation_date', 'Products', 'VALUE']].reset_index(drop=True)

print(clean_food_ca.head())

final_food_ca = clean_food_ca.pivot(index='observation_date', columns='Products', values='VALUE')
final_food_ca.columns.name = None
final_food_ca = final_food_ca.rename(columns={
    "Milk, 4 litres": "avg price milk (CA)",
    "Dry beans and legumes, 900 grams ": "avg price dried beans (CA)",
})

final_food_ca = final_food_ca[['avg price dried beans (CA)', 
                                   'avg price milk (CA)']]
final_food_ca.reset_index(inplace=True)
final_food_ca['observation_date'] = pd.to_datetime(final_food_ca['observation_date'])

base_year = 2017
base_prices = final_food_ca[final_food_ca['observation_date'].dt.year == base_year]

base_milk_ca = base_prices['avg price milk (CA)'].iloc[0]
final_food_ca['milk_ca_index'] = (final_food_ca['avg price milk (CA)'] / base_milk_ca) * 100

base_beans_ca = base_prices['avg price dried beans (CA)'].iloc[0]
final_food_ca['beans_ca_index'] = (final_food_ca['avg price dried beans (CA)'] / base_beans_ca) * 100

us_merged_price.reset_index(inplace=True)
us_merged_price['observation_date'] = pd.to_datetime(us_merged_price['observation_date'])

us_merged_price = pd.merge(us_merged_price, final_food_ca, on='observation_date', how='outer')

us_merged_price = us_merged_price.drop(columns=['index'])

us_merged_price.to_csv('./data/derived/us_merged_price.csv', index=False)

for col in us_merged_price.columns:
    print(col)

cpi_ca = pd.read_csv('./data/raw/food cpi - ca.csv')

food_cpi_ca = (
    cpi_ca[cpi_ca['Products and product groups'] == 'Food']
    .rename(columns={'REF_DATE': 'observation_date'})
    .drop(columns=['Products and product groups'])
    .rename(columns={'VALUE': 'food cpi (CA)'})
    .reset_index(drop=True)
)

food_cpi_ca['observation_date'] = pd.to_datetime(food_cpi_ca['observation_date'], format='%Y-%m')
food_cpi_ca = food_cpi_ca.set_index('observation_date')
food_cpi_ca.index = food_cpi_ca.index.strftime('%Y-%m') + '-01'
food_cpi_ca.index = pd.to_datetime(food_cpi_ca.index, format='%Y-%m-%d')
food_cpi_ca = food_cpi_ca[['food cpi (CA)']]

print(food_cpi_ca.head())

us_merged_price = pd.merge(us_merged_price, food_cpi_ca, on='observation_date', how='outer')

base_year = 2000
base_prices = us_merged_price[us_merged_price['observation_date'].dt.year == base_year]
base_food_cpi_ca = base_prices['food cpi (CA)'].iloc[0]
us_merged_price['food_cpi_ca_index'] = (us_merged_price['food cpi (CA)'] / base_food_cpi) * 100

us_merged_price.to_csv('./data/derived/us_merged_price.csv', index=False)

rearranged = [
    'observation_date', 'beef_price_index', 'beef_ca_index', 'beans_price_index', 'beans_ca_index', 
    'milk_price_index', 'milk_ca_index', 'food_cpi_index', 'food_ppi_index', 'food_cpi_ca_index', 
    'cheese_price_index', 'ice_cream_price_index', 
    'food cpi (CA)', 'avg price ground beef (US)', 'avg price ground beef (CA)',
    'avg price dried beans (US)', 'avg price dried beans (CA)',
    'avg price milk (US)', 'avg price milk (CA)', 'food cpi (US)', 'food ppi (US)', 
    'avg price cheddar cheese (US)', 'avg price ice cream (US)'
]

us_merged_price = us_merged_price[rearranged]

final_merged_index = us_merged_price[['observation_date', 'beef_price_index', 'beef_ca_index', 
                                     'beans_price_index', 'beans_ca_index', 'milk_price_index', 
                                     'milk_ca_index', 'food_cpi_index', 'food_ppi_index', 
                                     'food_cpi_ca_index', 'cheese_price_index', 'ice_cream_price_index']].copy()
final_merged_index['observation_date'] = pd.to_datetime(final_merged_index['observation_date'])
final_merged_index.set_index('observation_date', inplace=True)
final_merged_index = final_merged_index[(final_merged_index.index >= '1996-01-01') & 
                                                 (final_merged_index.index <= '2024-12-31')]

final_merged_index.to_csv("./data/derived/final_merged_index.csv", index=False)

style_mapping = {
    'beef_price_index': {'label': 'Beef (US)', 'color': '#1f77b4', 'linestyle': '-'},
    'beef_ca_index': {'label': 'Beef (CA)', 'color': '#ff7f0e', 'linestyle': '-'}, 
    'beans_price_index': {'label': 'Beans (US)', 'color': '#2ca02c', 'linestyle': '-'},
    'beans_ca_index': {'label': 'Beans (CA)', 'color': '#d62728', 'linestyle': '-'},
    'milk_price_index': {'label': 'Milk (US)', 'color': '#9467bd', 'linestyle': '-'},
    'milk_ca_index': {'label': 'Milk (CA)', 'color': '#8c564b', 'linestyle': '-'},
    'cheese_price_index': {'label': 'Cheese (US)', 'color': '#e377c2', 'linestyle': '-'},
    'ice_cream_price_index': {'label': 'Ice Cream (US)', 'color': '#7f7f7f', 'linestyle': '-'},
    'food_cpi_ca_index': {'label': 'Food (CA)', 'color': '#bcbd22', 'linestyle': '--'},
    'food_cpi_index': {'label': 'Food (US)', 'color': '#17becf', 'linestyle': '--'},
    'food_ppi_index': {'label': 'Food Manufacturing (US)', 'color': '#ff9896', 'linestyle': '--'},
}

plt.figure(figsize=(12, 6))
handles = []
labels = []
legend_order = [
    'beef_price_index', 'beef_ca_index',
    'beans_price_index', 'beans_ca_index',
    'milk_price_index', 'milk_ca_index',
    'cheese_price_index', 'ice_cream_price_index', 
    'food_cpi_ca_index', 'food_cpi_index', 'food_ppi_index'
]

for key in legend_order:
    if key in final_merged_index.columns:
        style = style_mapping[key]
        line, = plt.plot(final_merged_index.index, final_merged_index[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])
        
plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. & Canada: Overview of Food Price Changes')
plt.legend(handles, labels, loc='upper left', fontsize=10, frameon=True)
plt.grid(True)
plt.tight_layout()
plt.savefig('./data/figures/overview_price_changes.png', format='png')
plt.show()

style_mapping = {
    'beef_price_index': {'label': 'Beef (US)', 'color': 'blue', 'linestyle': '--'},
    'beef_ca_index': {'label': 'Beef (CA)', 'color': 'red', 'linestyle': '--'},
    'beans_price_index': {'label': 'Beans (US)', 'color': 'navy', 'linestyle': '--'},
    'beans_ca_index': {'label': 'Beans (CA)', 'color': 'darkred', 'linestyle': '--'},
    'milk_price_index': {'label': 'Milk (US)', 'color': 'dodgerblue', 'linestyle': '-'},
    'milk_ca_index': {'label': 'Milk (CA)', 'color': 'firebrick', 'linestyle': '-'},
    'cheese_price_index': {'label': 'Cheese (US)', 'color': 'purple', 'linestyle': '-'},
    'ice_cream_price_index': {'label': 'Ice Cream (US)', 'color': 'pink', 'linestyle': '-'}
}

plt.figure(figsize=(12, 6))
handles = []
labels = []

legend_order = [
    'beef_price_index', 'beef_ca_index',
    'beans_price_index', 'beans_ca_index',
    'milk_price_index', 'milk_ca_index',
    'cheese_price_index', 'ice_cream_price_index'
]

for key in legend_order:
    if key in final_merged_index.columns:
        style = style_mapping[key]
        line, = plt.plot(final_merged_index.index, final_merged_index[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])

plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. & Canada: Overview of Food Price Changes')
plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.show()

style_mapping = {
    'beef_price_index': {'label': 'US Ground Beef', 'color': 'blue', 'linestyle': '-'},
    'beans_price_index': {'label': 'US Dried Beans', 'color': 'navy', 'linestyle': '-'},
}

plt.figure(figsize=(12, 6))
handles, labels = [], []

for key in style_mapping:
    if key in final_merged_index.columns:
        style = style_mapping[key]
        line, = plt.plot(final_merged_index.index, final_merged_index[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])

plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. Price Changes: Beef vs. Beans')
plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('./data/figures/us_beef_beans.png', format='png')
plt.show()

style_mapping = {
    'beef_price_index': {'label': 'US Beef', 'color': 'blue', 'linestyle': '-'},
    'beef_ca_index': {'label': 'CA Beef', 'color': 'red', 'linestyle': '-'},
    'beans_price_index': {'label': 'US Beans', 'color': 'navy', 'linestyle': '-'},
    'beans_ca_index': {'label': 'CA Beans', 'color': 'darkred', 'linestyle': '-'}
}

plt.figure(figsize=(12, 6))
handles, labels = [], []

for key in style_mapping:
    if key in final_merged_index.columns:
        style = style_mapping[key]
        line, = plt.plot(final_merged_index.index, final_merged_index[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])

plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. & Canadian Price Trends for Beef & Beans')
plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.show()

subset_for_beans_ca = us_merged_price[(us_merged_price['observation_date'].dt.year >= 2017) &
                                      (us_merged_price['observation_date'].dt.year < 2022)]

style_mapping = {
    'beef_price_index': {'label': 'US Beef', 'color': 'indigo', 'linestyle': '-'},
    'beef_ca_index': {'label': 'CA Beef', 'color': 'forestgreen', 'linestyle': '-'},
    'beans_price_index': {'label': 'US Beans', 'color': 'mediumpurple', 'linestyle': '--'},
    'beans_ca_index': {'label': 'CA Beans', 'color': 'lightgreen', 'linestyle': '--'}
}

plt.figure(figsize=(12, 6))
handles, labels = [], []

for key in style_mapping:
    if key in subset_for_beans_ca.columns:
        style = style_mapping[key]
        
        line, = plt.plot(subset_for_beans_ca['observation_date'], subset_for_beans_ca[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. & Canadian Price Changes: Beef vs. Beans (2017-2022)')
plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('./data/figures/comparative_price_changes_2017_2022.png', format='png')
plt.show()

final_merged_index = final_merged_index.drop_duplicates(subset=['food_cpi_ca_index'])

style_mapping = {
    'beef_price_index': {'label': 'Beef (US)', 'color': 'indigo', 'linestyle': '-'},
    'beef_ca_index': {'label': 'Beef (CA)', 'color': 'forestgreen', 'linestyle': '-'},
    'food_cpi_ca_index': {'label': 'Food (CA)', 'color': 'mediumpurple', 'linestyle': '--'},
    'food_cpi_index': {'label': 'Food (US)', 'color': 'seagreen', 'linestyle': '--'}
}

plt.figure(figsize=(12, 6))
handles, labels = [], []

for key in style_mapping:
    if key in final_merged_index.columns:
        style = style_mapping[key]
        line, = plt.plot(final_merged_index.index, final_merged_index[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])
plt.axvspan('2001-03-01', '2001-11-01', color='gray', alpha=0.5, label='Recession')
plt.axvspan('2007-12-01', '2009-06-01', color='gray', alpha=0.5)
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. & Canada: Beef vs. Food Inflation')
plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('./data/figures/comparative_price_changes_vs_inflation.png', format='png')
plt.show()

style_mapping = {
    'beef_price_index': {'label': 'Beef (US)', 'color': 'indigo', 'linestyle': '-'},
    'food_ppi_index': {'label': 'Food Production (US)', 'color': 'red', 'linestyle': ':'},
}

plt.figure(figsize=(12, 6))
handles, labels = [], []

for key in style_mapping:
    if key in final_merged_index.columns:
        style = style_mapping[key]

        line, = plt.plot(final_merged_index.index, final_merged_index[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])
plt.axvspan('2001-03-01', '2001-11-01', color='gray', alpha=0.5, label='Recession')
plt.axvspan('2007-12-01', '2009-06-01', color='gray', alpha=0.5)
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. Inflation: Beef vs. Food Manufacturing')
plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('./data/figures/beef_vs_food_ppi.png', format='png')
plt.show()

style_mapping = {
    'beef_price_index': {'label': 'Ground Beef', 'color': 'indigo', 'linestyle': '-'},
    'beans_price_index': {'label': 'Dried Beans', 'color': 'mediumpurple', 'linestyle': '-'},
    'cheese_price_index': {'label': 'Cheddar Cheese', 'color': '#00BFFF', 'linestyle': '-'},
    'ice_cream_price_index': {'label': 'Ice Cream', 'color': '#87CEFA', 'linestyle': '-'},
    'milk_price_index': {'label': 'Whole Milk', 'color': '#B0E0E6', 'linestyle': '-'},
    'food_ppi_index': {'label': 'Food Production', 'color': 'red', 'linestyle': ':'},
}

plt.figure(figsize=(12, 6))
handles, labels = [], []

for key in style_mapping:
    if key in final_merged_index.columns:
        style = style_mapping[key]
        line, = plt.plot(final_merged_index.index, final_merged_index[key], 
                         label=style['label'], color=style['color'], linestyle=style['linestyle'])
        handles.append(line)
        labels.append(style['label'])
plt.axvspan('2001-03-01', '2001-11-01', color='gray', alpha=0.5, label='Recession')
plt.axvspan('2007-12-01', '2009-06-01', color='gray', alpha=0.5)
plt.axvspan('2020-02-01', '2020-04-01', color='gray', alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Price Index')
plt.title('U.S. Inflation: Beef vs. Other Foods')
plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('./data/figures/beef_vs_other_foods.png', format='png')
plt.show()

for col in final_merged_index.columns:
    print(col)

final_merged_index = final_merged_index.reset_index()

print(list(final_merged_index.columns))

selected_years = [2004, 2008, 2012, 2016, 2020]
categories = ['beef_price_index', 'beef_ca_index', 'beans_price_index', 'milk_price_index', 
              'cheese_price_index', 'food_cpi_index', 'food_ppi_index']

summary_statistics = []

for category in categories:
    previous_mean = None
    
    for year in selected_years:
        filtered_data = final_merged_index[final_merged_index['observation_date'].dt.year == year][category]
        
        mean_price = filtered_data.mean()
        std_dev_price = filtered_data.std()
        num_obs = filtered_data.count()

        if previous_mean is not None:
            percentage_change = ((mean_price - previous_mean) / previous_mean) * 100
        else:
            percentage_change = None
        
        summary_statistics.append({
            'Category': category.replace('_', ' ').title(),
            'Year': year,
            'Price (Mean)': mean_price,
            'Price (Standard Deviation)': std_dev_price,
            'Nb. Obs.': num_obs,
            'Percentage Change (%)': percentage_change
        })
        
        previous_mean = mean_price

summary_df = pd.DataFrame(summary_statistics)

print(summary_df)

summary_df.to_excel('./data/figures/summary_statistics.xlsx', index=False)

final_merged_index = final_merged_index.reset_index(drop=True)

final_merged_index['observation_date'] = pd.to_datetime(final_merged_index['observation_date'])

final_merged_index = final_merged_index.sort_values('observation_date')

final_merged_index['collusion'] = np.where(
    ((final_merged_index['observation_date'] >= '2002-01-01') & (final_merged_index['observation_date'] <= '2006-12-31')) |
    ((final_merged_index['observation_date'] >= '2010-01-01') & (final_merged_index['observation_date'] <= '2015-12-31')) |
    (final_merged_index['observation_date'] >= '2021-01-01'),
    1, 0
)

price_cols = ['beef_price_index', 'beans_price_index', 'milk_price_index', 
              'cheese_price_index', 'beef_ca_index', 'food_cpi_index', 'food_ppi_index']

for col in price_cols:
    final_merged_index['log_' + col] = np.log(final_merged_index[col])

final_merged_index['growth_beef'] = final_merged_index['log_beef_price_index'] - final_merged_index['log_beef_price_index'].shift(1)
final_merged_index['growth_beans'] = final_merged_index['log_beans_price_index'] - final_merged_index['log_beans_price_index'].shift(1)
final_merged_index['growth_milk'] = final_merged_index['log_milk_price_index'] - final_merged_index['log_milk_price_index'].shift(1)
final_merged_index['growth_cheese'] = final_merged_index['log_cheese_price_index'] - final_merged_index['log_cheese_price_index'].shift(1)
final_merged_index['growth_beef_ca'] = final_merged_index['log_beef_ca_index'] - final_merged_index['log_beef_ca_index'].shift(1)
final_merged_index['growth_food_cpi'] = final_merged_index['log_food_cpi_index'] - final_merged_index['log_food_cpi_index'].shift(1)
final_merged_index['growth_food_ppi'] = final_merged_index['log_food_ppi_index'] - final_merged_index['log_food_ppi_index'].shift(1)

final_merged_index = final_merged_index.dropna(subset=['growth_beef', 'growth_beans', 'growth_beef_ca',
                                                       'growth_food_cpi', 'growth_food_ppi'])

final_merged_index['diff_growth_beef_beans'] = final_merged_index['growth_beef'] - final_merged_index['growth_beans']
final_merged_index['diff_growth_beef_beef_ca'] = final_merged_index['growth_beef'] - final_merged_index['growth_beef_ca']
final_merged_index['growth_milk_cheese'] = (final_merged_index['growth_milk'] + final_merged_index['growth_cheese']) / 2
final_merged_index['diff_growth_beef_milk_cheese'] = final_merged_index['growth_beef'] - final_merged_index['growth_milk_cheese']

X_beans = final_merged_index[['collusion', 'growth_food_cpi', 'growth_food_ppi']]
X_beans = sm.add_constant(X_beans)
y_diff_beans = final_merged_index['diff_growth_beef_beans']
model_beef_beans = sm.OLS(y_diff_beans, X_beans, missing='drop').fit()
print("=== DiD Regression: US Beef vs. Beans ===")
print(model_beef_beans.summary())
summary_beef_beans = model_beef_beans.summary().tables[1]
summary_df = pd.DataFrame(summary_beef_beans.data[1:], columns=summary_beef_beans.data[0])
summary_df.to_excel("./data/figures/reg_beef_vs_beans.xlsx", index=False)

X_beef_ca = final_merged_index[['collusion', 'growth_food_cpi', 'growth_food_ppi']]
X_beef_ca = sm.add_constant(X_beef_ca)
y_diff_beef_ca = final_merged_index['diff_growth_beef_beef_ca']
model_beef_ca = sm.OLS(y_diff_beef_ca, X_beef_ca, missing='drop').fit()
print("=== DiD Regression: US Beef vs. CA Beef ===")
print(model_beef_ca.summary())
summary_beef_ca = model_beef_ca.summary().tables[1]
summary_df_beef_ca = pd.DataFrame(summary_beef_ca.data[1:], columns=summary_beef_ca.data[0])
summary_df_beef_ca.to_excel("./data/figures/reg_beef_vs_beef_ca.xlsx", index=False)

X_milk_cheese = final_merged_index[['collusion', 'growth_food_cpi', 'growth_food_ppi']]
X_milk_cheese = sm.add_constant(X_milk_cheese)
y_diff_milk_cheese = final_merged_index['diff_growth_beef_milk_cheese']
model_beef_milk_cheese = sm.OLS(y_diff_milk_cheese, X_milk_cheese, missing='drop').fit()
print("=== DiD Regression: US Beef vs. Dairy ===")
print(model_beef_milk_cheese.summary())
summary_beef_milk_cheese = model_beef_milk_cheese.summary().tables[1]
summary_df_beef_milk_cheese = pd.DataFrame(summary_beef_milk_cheese.data[1:], columns=summary_beef_milk_cheese.data[0])
summary_df_beef_milk_cheese.to_excel("./data/figures/reg_beef_vs_milk_cheese.xlsx", index=False)