<?php

class Solution {

    // function blockXYIndex($x, $y)
    // {
    //     if ($x == 0)
    // }

    /**
     * @param String[][] $board
     * @return NULL
     */
    function solveSudoku(&$board) {

        $rows = $board;
        $cols = [];
        $blocks = [];


        // create cols data set
        for ($i = 0; $i < 9; $i++)
        {
            $col = [];

            foreach ($board as $index => $row)
            {
                $col[] = $row[$i];
            }

            $cols[] = $col;
        }

        // create blocks data set
        for ($i = 0; $i < 9; $i += 3)
            for ($j = 0; $j < 9; $j += 3)
            {
                $block = [];

                for ($x = $i; $x < $i + 3; $x++)
                    for ($y = $j; $y < $j + 3; $y++)
                    {
                        // $_x = $x + $i;
                        // $_y = $y + $i;

                        $block[] = $rows[$x][$y];

                        // $block[] = $rows[$_x][$_y];
                        // $block[] = $col[$_y][$_x];
                    }

                $blocks[] = $block;
                // print_r($block);
                // exit;
            }

        // print_r($blocks);
        // exit;


        // print_r($cols);
        // exit;

        $output = [];



        // backtracking
        $track = [
            [] // x,y,block,block_i
        ];


        $backtrack = 0;
        $backtrack = [
            // [0, 0, -1, 0], // x, y, block, val
        ];


        $log = [
            // [0, 0, -1, 0], // x, y, block, val
            [-1, -1, -1, 0]
        ];

        // $last_log_val = 0;

        // replace dots with number for row+col based on index
        $counter = 0;
        for ($x = 0; $x < 9; $x++)
            for ($y = 0; $y < 9; $y++)
            {
                // echo $x .' '. $y ."\n";

                $square = $rows[$x][$y];

                // if (!in_array($counter, $log))
                // if (!array_key_exists($counter, $log))
                if ($square == '.')
                    if (!array_key_exists($x .'-'. $y, $log))
                    {
                        $log[$x .'-'. $y] = [
                        // $log[$counter] = [
                            'x' => $x,
                            'y' => $y,
                            'b' => -1,
                            'val' => ($rows[$x][$y] != '.') ? $rows[$x][$y] : 0
                        ];
                    }
                    else
                    {
                        // echo "key exists \n";
                    }




                // echo $square ."\n";
                // continue;

                $row = $rows[$x];
                $col = $cols[$y];


                $block_index = 0;

                if ($y < 3)
                {
                    if ($x < 3) $block_index = 0;
                    if ($x > 2 && $x < 6) $block_index = 3;
                    if ($x > 5) $block = $block_index = 6;
                }

                if ($y > 2 && $y < 6)
                {
                    if ($x < 3) $block_index = 1;
                    if ($x > 2 && $x < 6) $block_index = 4;
                    if ($x > 5) $block_index = 7;
                }

                if ($y > 5)
                {
                    if ($x < 3) $block_index = 2;
                    if ($x > 2 && $x < 6) $block_index = 5;
                    if ($x > 5) $block_index = 8;
                }

                $block = $blocks[$block_index];

                // $log[$counter]['b'] = $block_index;
                if (array_key_exists($x .'-'. $y, $log))
                 $log[$x .'-'. $y]['b'] = $block_index;


                // $block = $blocks[]

                // echo $square ."\n";
                // print_r($row) ."\n";
                // print_r($col) ."\n";
                // print_r($block) ."\n";
                // break 2;

                $backtrack_action = false;
                if ($square == '.')
                {
                    $found = false;
                    $block_i = 0;
                    for ($n = 1; $n <= 9; $n++)
                    {
                        // check that number doesn't exist in current row/col/block
                        if (in_array($n, $row)
                        || in_array($n, $col)
                        || in_array($n, $block))
                            continue;

                        // if ($n <= $log[$counter]['val'])
                        if ($n <= $log[$x .'-'. $y]['val'])
                        // if ($n <= $backtrack['val'])
                            continue;

                        $found = true;


                        // update rows, cols, blocks
                        // $square = $rows[$x][$y];
                        $rows[$x][$y] = $n;
                        $cols[$y][$x] = $n;

                        for ($k = 0; $k < count($blocks[$block_index]); $k++)
                            if ($blocks[$block_index][$k] == '.')
                            {
                                $block_i = $k;
                                $blocks[$block_index][$k] = $n;
                                break;
                            }


                        // print_r($rows[$x]);
                        // print_r($cols[$y]);
                        // print_r($blocks[$block_index]);
                        // exit;

                        $output[$x][$y] = "". $n;
                        // $board[$x][$y] = $n;

                        // update log
                        // $log[$counter]['val'] = $n;
                        $log[$x .'-'. $y]['val'] = $n;

                        // store last log value
                        // $last_log_val = $n;

                        // reset backtrack
                        // $backtrack = 0;

                        // $counter++;

                        break;
                    }

                    if (!$found)
                    {
                        // echo "no possible combination. backtrack. \n";


                        // handle the first square (can't backtrack before)
                        // if (count($log) == 0)
                        // {
                        //     $__prev = $log;
                        //     echo "can't backtrack further \n";
                        //     exit;
                        // }
                        // else
                        // {
                            // remove last add
                            $__prev = array_slice($log, -2, 1);
                        // }




                        $__prev_index = null;
                        foreach ($__prev as $index => $array)
                        {
                            $__prev_index = $index;
                            break;
                        }

                        $__prev = $__prev_index;

                        // echo $__prev_index;

                        // print_r($__prev);
                        // exit;

                        // print_r($blocks[$log[$__prev]['b']]);

                        $rows[$log[$__prev]['x']][$log[$__prev]['y']] = '.';
                        $cols[$log[$__prev]['y']][$log[$__prev]['x']] = '.';
                        // $blocks[$log[$__prev]['b']] = '.'; // this is wrong- it deletes the complete block

                        // remove val from block
                        for ($r = 0; $r < count($blocks[$log[$__prev]['b']]); $r++)
                        {
                            if ($blocks[$log[$__prev]['b']][$r] == $log[$__prev]['val'])
                            {
                                $blocks[$log[$__prev]['b']][$r] = '.';
                                break;
                            }
                        }

                        // print_r($log[$__prev]['b']);

                        // print_r($blocks[$log[$__prev]['b']]);
                        // exit;

                        // delete last log
                        // unset($log[$__prev]);

                        // if (count($log) > 1)
                            array_pop($log);

                        // print_r($rows[$x]);
                        // print_r($cols[$y]);
                        // print_r($blocks[$block_index]);

                        /*
                        $goback = 2;

                        if ($y - $goback < -1)
                        {
                            $x = $x - $goback;
                        }
                        else
                        {
                            $y = $y - $goback;
                        }
                        */

                        // $last = null;
                        /*
                        for ($b = 2; $b <= 9; $b++)
                        {
                            if ($y - $b < 0)
                                $x = $x - $b;
                            else
                                $y = $y - $b;

                            if (array_key_exists($x .'-'. $y, $log))
                            {
                                // echo 'found x: '. $x .' y:'. $y ."\n";
                                break;
                            }

                        }
                        */
                        $__prev = array_slice($log, -2, 1);

                        $__prev_index = null;
                        foreach ($__prev as $index => $array)
                        {
                            $__prev_index = $index;
                            break;
                        }

                        $__prev = explode('-', $__prev_index);
                        // print_r($__prev);

                        $x = $__prev[0];
                        $y = $__prev[1];

                        // Go back one more step to rewrite 0, otherwise the first loop will always be skipped
                        if ($y == 0)
                            $y = -1;

                        // echo $__prev = $__prev_index ."\n";


                        // $x = -1;
                        // $y = -1;
                        // $counter = 0;
                        // echo 'backtrack to x: '. $x .' y: '.  $y ."\n";


                        continue;

                        /*
                        exit;

                        // echo 'problem adding x: '. $x .' y: '. $y;
                        // exit;

                        $backtrack_action = true;

                        // reverse previous rows cols blocks
                        // $counter--;

                        // $backtrack++;
                        // echo 'backtrack: '. $backtrack ."\n";




                        // remove last log because it blocks the backtracking
                        unset($log[count($log) - 1]);

                        $backtrack = $log[count($log) - 1];

                        // reset last square
                        // $__prev = count($log) - (intval($backtrack) + 1);
                        // $__prev = count($log) - 1;
                        // $rows[$log[$__prev]['x']][$log[$__prev]['y']] = '.';
                        // $cols[$log[$__prev]['y']][$log[$__prev]['x']] = '.';
                        // reset last square for blocks
                        // $blocks[$block_index][$block_i] = '.'; // this is current square
                        // $blocks[$log[$__prev]['b']] = '.';

                        // delete current square when changing previous one
                        // $log[count($log) - 1]['val'] = 0;

                        // backtrack last square to try another value greater than last one

                        echo 'current x: '. $x .' y: '. $y ."\n";

                        // $x = $log[count($log) - (intval($backtrack) + 2)]['x'];
                        // $y = $log[count($log) - (intval($backtrack) + 2)]['y'];

                        // $x = $log[count($log) - 2]['x'];
                        // $y = $log[count($log) - 2]['y'];
                        // echo 'backtrack to x: '. $x .' y: '.  $y ."\n";


                        // $x = array_slice($log, -2, 1)['x'];
                        // $y = array_slice($log, -2, 1)['y'];

                        // echo 'backtrack to x: '. $x .' y: '.  $y ."\n";

                        // restart loop
                        $goback = 3;

                        if ($y - $goback < -1)
                        {
                            $x = $x - $goback;
                        }
                        else
                        {
                            $y = $y - $goback;
                        }

                        // $x = -1;
                        // $y = -1;
                        // $counter = 0;
                        // echo 'backtrack to x: '. $x .' y: '.  $y ."\n";


                        continue;
                        */


                        // exit;
                    }

                    // $output[$x][$y] = $rows[$x][$y];
                }
                else
                {
                    $output[$x][$y] = $rows[$x][$y];
                    // $counter++;
                }

                // print_r($log[$counter]);
                // print_r($log[$x .'-'. $y]);

                // if (!$backtrack_action)
                    $counter++;


                // if ($counter >= 100)
                    // break 2;

                // if ($x > 2)
                    // break 2;
            }

        // print_r($log);
        // print_r($output);
        // return json_encode($output);

        // exit;

        // echo $output;

        // return $output;

        // exit;
        // print_r($output);

        foreach ($output as $i => $row)
        {
            foreach ($row as $j => $col)
            {
                $output[$i][$j] = "". $output[$i][$j];
                // echo $col ." ";
            }
            // echo "\n";
        }

        $board = $output;
        return;


        exit;

        $counter = 0;
        for ($y = 0; $y < 9; $y++)
        {
            // print_r($rows[$i]);
            // exit;

            for ($x = 0; $x < 9; $x++)
            {
                $no = $rows[$y][$x];

                if ($no == '.')
                {
                    // echo 'x: '. $x .', y: '. $y;
                    // exit;

                    // try all combinations where number not repeated on x
                    for ($n = 1; $n <= 9; $n++)
                    {
                        // check that number doesn't exist in current row & col
                        // if (!in_array($n, $rows[$y]))
                        if (!in_array($n, $rows[$y])
                        && !in_array($n, $cols[$x])
                        && !in_array($n, $blocks[$x]))
                        {
                            $rows[$y][$x] = $n;
                            // break;
                        }
                    }

                }

//                 $_row = $rows[$i][$j];
//                 $_col = $cols[$j][$i];

//                 echo $_row ."\n";
//                 echo $_col ."\n";

                // $counter++;
                // if ($counter > 1) exit;
            }

            print_r($rows[$y]);
            // exit;
        }





        // $counter = 0;
        // create cols
        for ($i = 0; $i < 9; $i++) // rows
        {
            $col = [];

            for ($j = 0; $j < 9; $j++) // cols
            {
                $counter++;

                $col[] = $board[$i][$j];

                // try a number that doesn't exist
//                 if ($board[$i][$j] == '.')
//                 {
//                     $exists = [];
//                     // for ($k = 0; $k < 9; $k++)
//                         // $exists[] = $board[$i][$k];

//                     print_r($k);
//                     exit;
//                 }

                // echo $rows[$i][$j] ."\n";

//                 if ($j != '.')
//                 {

//                 }


                // if ($counter >= 2) break;
            }

            // print_r($col);
            $cols[] = $col;

            // break;
        }


        print_r($col);

    }
}
