#filtering through the listings to see which listings are the closest match according to the main GPU CSV
#looping through main GPU CSV df to match with other df's
for gpu_index, gpu_row in gpu_csv.iterrows():
    #removing extra fluff the main csv writes
    gpu_name = gpu_row['name'].lower().split('graphics card')[0]
    test = len(gpu_row['keywords'])
    count = 0
    #grabbing extra variables for the search
    brand = gpu_row['brand'].lower()
    model_num = [num for num in gpu_row['keywords'] if num.isdigit()]
    #loop through the microcenter df
    for mc_index, mc_row in mc_df.iterrows():
        mc_name = mc_row['name'].lower().split('graphics card')[0]
        #loop through the keywords for the search
        for keyword in gpu_row['keywords']:
            if keyword in mc_row['name']:
                count += 1
            if count == test and (brand in mc_name):
                #using the match score created by StubHub to find how relative the listings are
                match_score = fuzz.ratio(gpu_name, mc_name)
                #from the tests used any listing over a match score of 50 would give a similar/relative listing
                if match_score >= 50:
                    gpu_mc_names.append(gpu_row['name'])
                    mc_names.append(mc_name)
                    match_scores.append(match_score)
                    model_number.append(''.join(model_num))
                    mc_price.append(mc_row['prices'])
                count = 0
        else:
            next