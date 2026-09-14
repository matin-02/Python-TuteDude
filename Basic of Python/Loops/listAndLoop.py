countries = ['India' , 'france' , 'germany' , 'usa' , 'dutch' , 'pakistan' , 'switzerland','uae' ,'dubai']

# countries starting with the 'd'
# also, print all these countries as a list
counter = 0
output = []
for country in countries:
    if country[0] ==  "d" :
        counter += 1
        output.append(country)
print(counter)
print(output)