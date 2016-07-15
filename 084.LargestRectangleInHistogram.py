'''
 by  tim9216,  tim9216,  tim9216
 i am looking for a job in  shang-hai,  china
 contact me with the above ID on gmail.  中文见 weibo.com/tim9216
 DO  NOT NOT NOT NOT NOT NOT NOT NOT NOT  REMOVE THIS PIECE OF INFORMATION

 this programme solves the problem  "the largest rectangle in histogram"  on leet code
 http://leetcode.com/problems/largest-rectangle-in-histogram   and

 IMPROVES the solution to its extended problem proposed by chen li-ren by TWO DEGREES
 http://www.weibo.com/1915548291/DCEHQ9wa8
 
 SEE CORRESPONDING  C++  SOLUTION FOR BETTER COMMENTS
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        return  largest_area(heights)



'''
 solution to the problem  "the largest rectangle in histogram"  on leet code
 http://leetcode.com/problems/largest-rectangle-in-histogram
'''
def  largest_area( heights ): 
    heights.append(-1)
    max_area  =  0
    ascension =  []   # as stack
    length    =  len(heights)
    for  i  in  range( 0, length ):

        while  0 < len(ascension)  and  heights[ ascension[-1] ]  >  heights[i]  :
            boundaryH =  heights[ ascension[-1] ]
            ascension.pop()

            area =  boundaryH * i  if 0 == len(ascension) else   boundaryH  *  ( i - ascension[-1] - 1 )

            if  max_area < area  :
                max_area = area

        ascension.append(i)

    heights.pop()
    return max_area


################################################################################################################
#######################################  EXTRA FOR EXTENDED 3D-HITOGRAM  #######################################
################################################################################################################

'''
 by  tim9216,  tim9216,  tim9216
 i am looking for a job in  shang-hai,  china
 contact me with the above ID on gmail.  中文见 weibo.com/tim9216
 DO  NOT NOT NOT NOT NOT NOT NOT NOT NOT  REMOVE THIS PIECE OF INFORMATION

 IMPROVED solution to the extended problem proposed by chen li-ren by TWO DEGREES,
 based on the leed code problem "the largest rectangle in histogram"
 http://www.weibo.com/1915548291/DCEHQ9wa8
'''
def  largest_volume( original_heights ):
    max_area =  0
    length =  len( original_heights )
    width  =  len( original_heights[0] )


    # 3D-histogram MATRIX TRANSITION to ensure width < length
    if  width <= length  :
        h =  original_heights
    else:
        # transit matrix
        h =  []
        for y in range(0, width):
            h.append( [] )
            for x in range(0, length):
                low =  h[y][x]
                h[y].append( original_heights[x][y] )
        width, length =  length, width        # swapping 

    # VALLEY LOOPS
    # valley[y][x][span] as  3-dimensional arrays
    # denotes the valley in row y, in range [ x, x+range ], inclusive
    valley =  [  [  0  for  x in  range(width) ]  for y in range(length)   ]
    for  y  in  range( 0, length ):
        for  x  in  range( 0, width ):
            valley[y][x] =  [  0  for  x0 in  range(width-x) ]
            low = h[y][x]
            for  span  in  range( 0, width-x ):
                if  h[y][ x+span ]  <  low  :
                    low =  h[y][ x+span ]
                valley[y][x][span] =  low

    # SEARCH VERTICAL HISTOGRAM consists of valleys of aligned ranges in rows
    max_volume =  0
    for  x  in  range( 0, width ):
        for  span  in  range( 0, width-x ):
            partial_row_vol =  []
            for  y  in  range( 0, length ):
                partial_row_vol.append(  valley[ y ][ x ][ span ]  )

            volume =  ( span+1 )  *  largest_area( partial_row_vol )
            if  max_volume  <  volume:
                max_volume =  volume

    return  max_volume


################################################################################################################
###############################  TEST CASES GENERATION FOR EXTENDED 3D-HITOGRAM  ###############################
################################################################################################################

variation = [
    [ 0, 0, 0, 0, 0 ], 
    [ 0, 1, 2, 3, 4 ], 
    [ 4, 3, 2, 1, 0 ], 
    [ 0, 1, 1, 1, 1 ], 
    [ 0, 0, 0, 0, 1 ], 
    [ 0, 0, 1, 1, 1 ], 
    [ 1, 1, 0, 0, 0 ], 
    [ 0, 0, 1, 2, 3 ], 
    [ 3, 2, 1, 0, 0 ], 
    [ 0, 1, 2, 2, 2 ], 
    [ 2, 2, 2, 1, 0 ], 
    [ 0, 2, 4, 3, 1 ], 
    [ 0, 1, 4, 3, 2 ], 
    [ 0, 1, 3, 4, 2 ], 
    [ 0, 4, 3, 1, 2 ], 
    [ 0, 4, 2, 1, 3 ], 
    [ 0, 3, 1, 2, 4 ], 
    [ 0, 2, 1, 3, 4 ], 
    [ 0, 0, 1, 1, 1, 1 ], 
    [ 1, 1, 0, 0, 0, 0 ], 
    [ 1, 1, 1, 0, 0, 0 ],
    [ 0, 1, 2, 3, 4, 5, 6 ],
    [ 0, 1, 2, 3, 4, 5, 6, 5 ],
    [ 0, 1, 2, 3, 4, 5, 6, 6, 6, 6, 5, 4, 3, 2, 1 ]
]


'''
 by  tim9216,  tim9216,  tim9216
 i am looking for a job in  shang-hai,  china
 contact me with the above ID on gmail.  中文见 weibo.com/tim9216
 DO  NOT NOT NOT NOT NOT NOT NOT NOT NOT  REMOVE THIS PIECE OF INFORMATION
'''

def  build_case(  width, length,  x_variation, y_variation, x_section_delta, y_section_delta  ):
    h =   [   [ 0 for x in range(width) ]   for y in range(length)   ]

    yvarlen =  len( y_variation )
    xvarlen =  len( x_variation )
    y_sect  =  0
    for  y_stage  in  range( 0, length, yvarlen ) :
        y_base   =  y_stage // yvarlen  * y_section_delta
        y_offset =  0
        for  y_offset  in   range( 0, yvarlen ) :
            y =  y_stage + y_offset
            if  length <= y  :  break

            row_head =  y_base  +  y_variation[ y_offset ]

            for   x_stage  in  range( 0, width, xvarlen ):
                x_base   =   row_head   +   x_stage // xvarlen  *  x_section_delta
                x_offset =   0
                for  x_offset  in range( 0, xvarlen ):
                    x =  x_offset + x_stage
                    if  width <= x  :  break

                    h[y][x] =  x_base  +  x_variation[ x_offset ]
    return  h

def  show_case( heights ):
    length =  len( heights )
    width  =  len( heights[0] )
    for row in heights:
        for v in row:
            print format(v, '02'),
        print
    print

# buildup 3D histogram width=160, height=200
test_case =  build_case( 320, 400, variation[0], variation[-3], 1, 1 )
print largest_volume( test_case )

'''
 by  tim9216,  tim9216,  tim9216
 i am looking for a job in  shang-hai,  china
 contact me with the above ID on gmail.  中文见 weibo.com/tim9216
 DO  NOT NOT NOT NOT NOT NOT NOT NOT NOT  REMOVE THIS PIECE OF INFORMATION

'''

