from min_max_touches import draw_rect, find_max_min_square_count

# This class allows running tests on products with a given resolution and grid checking the x-2x rule.
# x-2x rule is a rule where the max squares touched by a square should not exceed twice the minimum in order for the
# product to be ok.

to_plot = True
grid_width = 80
grid_length = 80
grid_spacing = 6

# draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches')
# draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches')

# HotPop 16x10.7x6.2

# 16x10.7
prod_length = 10.7
prod_width = 16

# to check specific rectangle
# a = point.Point(61.65, 34, 'black')
# b = point.Point(69.216, 41.566, 'black')
# c = point.Point(50.336, 45.313, 'black')
# d = point.Point(57.902, 52.879, 'black')
# g = grid.Grid(grid_length, grid_width, grid_spacing)
# num_of_squares_touched =  find_num_of_squares_touching(a, b, c, d, g, prod_length, prod_width, True)
# min_pnts
# 61.65 69.21604255869606 50.33629150101524 57.90233405971131
# 34.0 41.566042558696054 45.31370849898476 52.879751057680814



min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('HotPop 16x10.7')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches HotPop 16x10.7')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches HotPop 16x10.7')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(max_pnts[0].x, max_pnts[1].x, max_pnts[2].x, max_pnts[3].x)
print(max_pnts[0].y, max_pnts[1].y, max_pnts[2].y, max_pnts[3].y)


# 16x6.2
prod_length = 6.2
prod_width = 16
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('HotPop 16x6.2')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches HotPop 16x6.2')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches HotPop 16x6.2')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(max_pnts[0].x, max_pnts[1].x, max_pnts[2].x, max_pnts[3].x)
print(max_pnts[0].y, max_pnts[1].y, max_pnts[2].y, max_pnts[3].y)

# 10.7x6.2
prod_length = 10.7
prod_width = 6.2
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('HotPop 6.2x10.7')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches HotPop 6.2x10.7')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches HotPop 6.2x10.7')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(max_pnts[0].x, max_pnts[1].x, max_pnts[2].x, max_pnts[3].x)
print(max_pnts[0].y, max_pnts[1].y, max_pnts[2].y, max_pnts[3].y)


# HotPop 16x10.7
# 24 38
# min_pnts
# 59.65 48.95040742321338 59.789624567973995 49.09003199118736
# 32.0 31.90662607016737 16.00060923097326 15.907235301140702
# max_pnts
# 59.65 67.21604255869606 70.96370849898474 78.52975105768077
# 32.7 25.133957441303963 44.01370849898478 36.447665940288715
# HotPop 16x6.2
# 18 28
# min_pnts
# 61.9 61.35963439496453 45.96088483053207 45.4205192254966
# 32.0 38.176407128168805 30.605508116037473 36.781915244206296
# max_pnts
# 62.0 62.054104520089936 77.99939076902673 78.05349528911671
# 33.0 26.800236077002165 33.13962456797403 26.93986064497612
# HotPop 6.2x10.7
# 12 20
# min_pnts
# 59.65 58.717433552600056 53.47359287183115 52.541026424431244
# 36.9 47.55928326958167 36.35963439496453 47.01891766454619
# max_pnts
# 59.65 70.35 59.65 70.35
# 38.8 38.8 45.0 45.0



#

# FruityPebbles 30.8x19.6x5.2

# 30.8x19.6
prod_length = 30.8
prod_width = 19.6
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('FruityPebbles 30.8x19.6')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches FruityPebbles 30.8x19.6')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches FruityPebbles 30.8x19.6')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)

# 30.8x5.2
prod_length = 30.8
prod_width = 5.2
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('FruityPebbles 30.8x5.2')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches FruityPebbles 30.8x5.2')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches FruityPebbles 30.8x5.2')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)


# 19.6x5.2
prod_length = 19.6
prod_width = 5.2
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('FruityPebbles 19.6x5.2')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches FruityPebbles 19.6x5.2')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches FruityPebbles 19.6x5.2')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)

# Wisozky 13.7x7.3x7.8

# 13.7x7.3
prod_length = 13.7
prod_width = 7.3
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('Wisozky 13.7x7.3')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches Wisozky 13.7x7.3')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches Wisozky 13.7x7.3')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)

# 13.7x7.8
prod_length = 13.7
prod_width = 7.8
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('Wisozky 13.7x7.8')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches Wisozky 13.7x7.8')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches Wisozky 13.7x7.8')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)

# 7.3x7.8
prod_length = 7.8
prod_width = 7.3
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('Wisozky 7.8x7.3')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches Wisozky 7.8x7.3')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches Wisozky 7.8x7.3')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)

# Taanug 13.3x12.5x3.55

# 13.3x12.5
prod_length = 13.3
prod_width = 12.5
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('Taanug 13.3x12.5')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches Taanug 13.3x12.5')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches Taanug 13.3x12.5')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)

# 13.3x3.55
prod_length = 13.3
prod_width = 3.55
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('Taanug 13.3x3.55')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches Taanug 13.3x3.55')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches Taanug 13.3x3.55')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)

# 12.5x3.55
prod_length = 12.5
prod_width = 3.55
min_num_of_squares, max_num_of_squares, min_pnts, max_pnts = find_max_min_square_count(grid_length, grid_width, grid_spacing,
                                                                                       prod_length, prod_width, to_plot)

print('Taanug 12.5x3.55')
print(min_num_of_squares, max_num_of_squares)
draw_rect(min_pnts[0], min_pnts[1], min_pnts[2], min_pnts[3], grid_length, grid_width, grid_spacing, 'Minimum Touches Taanug 12.5x3.55')
draw_rect(max_pnts[0], max_pnts[1], max_pnts[2], max_pnts[3], grid_length, grid_width, grid_spacing, 'Maximum Touches Taanug 12.5x3.55')
print('min_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
print('max_pnts')
print(min_pnts[0].x, min_pnts[1].x, min_pnts[2].x, min_pnts[3].x)
print(min_pnts[0].y, min_pnts[1].y, min_pnts[2].y, min_pnts[3].y)
