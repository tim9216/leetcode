#include <iostream>
using std::cout;

/*
 * by  tim9216,  tim9216,  tim9216
 * i am looking for a job in  shang-hai, china;
 * contact me with the above ID on gmail;  中文见 weibo.com/tim9216
 * DO  NOT NOT NOT NOT NOT NOT NOT NOT NOT  REMOVE THIS PIECE OF INFORMATION
 *
 * this programme solves the problem  "the largest rectangle in histogram"  on leet code
 * http://leetcode.com/problems/largest-rectangle-in-histogram   and 

 * IMPROVES the solution to the extended problem proposed by chen li-ren by TWO DEGREES
 * http://www.weibo.com/1915548291/DCEHQ9wa8
*/


#include <algorithm>
#include <vector>
#include <stack>


using std::vector;
using std::stack;
using std::swap;


class Solution{
public:
    int  largestRectangleArea( vector<int>&  height  );
    int  largestCuboidVolume(  vector< vector<int> >&   height  );
}; //Solution{}



/*
 * by  tim9216,  tim9216,  tim9216
 * i am looking for a job in  shang-hai, china;
 * contact me with the above ID on gmail;  中文见 weibo.com/tim9216
 * DO  NOT NOT NOT NOT NOT NOT NOT NOT NOT  REMOVE THIS PIECE OF INFORMATION

 * solution to the problem  "the largest rectangle in histogram"  on leet code
 * http://leetcode.com/problems/largest-rectangle-in-histogram
 */
int  Solution ::  largestRectangleArea(  vector<int>&  height  )
{
    height.push_back( -1 );

    // stores parts of the histogram indices, indicating incremental heights
    stack< int >   ascending_height;

    int  boundaryH,  area,  max_area =  0;

    // process the histogram bars from left to right
    for(   int i = 0;   i < height.size();   ++i   ){

        // decrement bar encountered,  reversed-order process
        while(   !ascending_height.empty()   &&   (  boundaryH = height[ ascending_height.top() ]  )  >  height[i]   ){
            ascending_height.pop();

            area =  ascending_height.empty()   ?

                // as the decending left-most processed bar remained, calculate the rectangle area towards LEFT
                boundaryH  *  i   :

                // as one of the bars of processed increasing sequence, calculate the area towards RIGHT
                boundaryH  *  ( i - ascending_height.top() - 1 );

            if(  max_area < area  )   max_area =  area;
        }//while(  &&  )

        // by handling all the previous processed, higher bars, store the current, i-th bar
        ascending_height.push( i );

    }//for(i)

    height.pop_back();
    return max_area;
}//Solution ::  largestRectangleArea(1)




/*
 * by  tim9216,  tim9216,  tim9216
 * i am looking for a job in  shang-hai, china;
 * contact me with the above ID on gmail;  中文见 weibo.com/tim9216
 * DO  NOT NOT NOT NOT NOT NOT NOT NOT NOT  REMOVE THIS PIECE OF INFORMATION

 * IMPROVED solution to the extended problem proposed by chen li-ren by TWO DEGREES
 * based on the leed code problem  "the largest rectangle in histogram"
 * http://www.weibo.com/1915548291/DCEHQ9wa8
 */
int  Solution ::  largestCuboidVolume(  vector< vector<int> >&   original_height  )
{
    int  length =  original_height.size();
    int  width  =  original_height.front().size();

    vector< vector<int> >&  height =   length < width  ?
        vector< vector<int> >( width, vector<int>(length) )   :   original_height;

    // 3D-histogram MATRIX TRANSITION to ensure  width < length
    if(  length  <  width  ){
        for(  int y = 0;   y < length;   ++y   ){
            for(   int x = 0;   x < width;   ++x   ){
                height[x][y] =  original_height[y][x];
            }//for(x)
        }//for(y)

        swap( length, width );
    }//if( < )

    // VALLEY LOOPS
    // element valley[ y ][ x ][ span ] denotes the low height of array in  ROW y,  COLUMN [ x,  x + span ],  inclusive
    vector<  vector< vector<int> >  >    valley(  length,  vector< vector<int> >( width, vector<int>() )  );
    int  low;
    for(  int y = 0;  y < length;  ++y  ){
        for(  int x = 0;  x < width;  ++x  ){
            valley[y][x].reserve( width-x );
            low =  height[y][x];
            for(   int span = 0;   x+span < width;   ++span   ){
                if(  height[y][ x+span ]  <  low  ){
                    low =  height[y][ x+span ];
                }//if( < )
                //valley[y][x][span] =  low;
                valley[y][x].push_back( low );
            }//for( span )
        }//for(x)
        
    }//for(y)

    // SEARCH VERTICAL HISTOGRAM consists of valleys of aligned ranges in rows
    // enumerate all the possible  sub-ranges  of each row, in range [x, x+span],  as in nested x, span loop,  then
    // search along vertical direction for max rectangle in the histogram of valleys combination,  as in y loop
    vector< int >   valleys_in_aligned_range( length );
    int  volume,  max_volume =  0;
    for(  int x = 0;  x < width;  ++x  ){
        for(  int span = 0;  x + span < width;  ++span  ){

            for(  int y = 0;  y < length;  ++y  ){
                valleys_in_aligned_range[y] =  valley[y][x][span];
            }//for(y)
            
            volume =   ( span + 1 )  *  largestRectangleArea( valleys_in_aligned_range );
            if(  max_volume < volume  ){
                max_volume =  volume;
            }//if( max_volume < )

        }//for(span)
    }//for(x)

    return  max_volume;
}//Solution :: largestCuboidVolume(1)
