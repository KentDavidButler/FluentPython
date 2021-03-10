# Cartesian Product
# compared to Java, where multipule for loops may solve this,
# with python we can produce the same result in one line


colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts

# java style for comparison

# colors_j = ['black', 'white']
# sizes_j = ['S', 'M', 'L']
#
# for (int i=0; i <= colors_j.length; i++) {
#     for (int j=0; j <= sizes_j.length; j++)
#     {
#         tshirts.append(colors_j[i], sizes_j[j])
#     }
#
# }
