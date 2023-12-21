Welcome to another day of me restarting 162 times and pulling an answer out of nowhere.

Skip to the bottom to figure out which file holds my solution ↓↓↓

Wanna know what I did?

First, color the input character-by-character like a checkerboard.
All the WHITE squares are squares that you can reach by moving an EVEN number of times.
All the BLACK squares are squares that you can reach by moving an ODD number of times.

If you didn't bother to look, the input has a perfect rhombus of uninterrupted garden plots ('.').

Then, the input can be split into three parts, which I'll call W, B, and R:
    W. The WHITE-colored characters inside the rhombus (i.e. the answer to part one)
    B. The BLACK-colored characters inside the rhombus (i.e. the answer to part one if you use 65 instead of 64)
    R. The rest (everything OUTSIDE the rhombus)
        (i.e. the total number of garden plots in the input minus (W + B))


Let S be the number of steps the elf needs to travel (26501365)
Notice that S mod 131 = 65.

This means that as long as the garden plots that the elf needs to reach forms a perfect rhombus,
    you can break up that rhombus into the parts I've already mentioned. You can convince yourself of that
    by drawing a picture or by not caring.

Let L be the number of additional layers of thickness 131
that we are adding on to the rhombus considered in part one.
For part one, L = 0.
If S = 196, then L = floor(196 ÷ 131) = 1.
However, S = 26501365, so L = floor(26501365 ÷ 131) = 202300

Here are some facts:

    The number of W-regions within S steps of the start is L²
    The number of B-regions within S steps of the start is (L + 1)²
    The number of R-regions within S steps of the start is L(L + 1)

The justifications of these facts are trivial and are left as an exercise to the reader.

Finally, when you look at W × L² + B × (L + 1)² + R × L(L + 1), you get... the wrong answer!!!

Luckily, I had already brute forced the answers for S = 196 and S = 327 (which are both ≡ 65 (mod 131)),
so I recognized that the answers that my new algorithm returned for those values were wrong.

Having just discovered that the number of R-regions is L(L + 1), I was suspiciously quick to notice that
the incorrect answers I got differed from the correct ones by 10 × L(L + 1)

I still have no idea where the error came from, but I assume it has to do with overlapping perimeters.

Anyway, the final formula was W × L² + B × (L + 1)² + R × L(L + 1) - 10 × L(L + 1).

----------------------------------------------------------------------------------------------------------------

Now why do I have so many files in this folder?

Here's what each one is:
    drawer.py:              a script that maps a simpler version of part two to output.txt
    input.txt:              my puzzle input
    output.txt:             the ouput of drawer.py, a map of all garden plots within 196 steps of the start
    part1.py:               my original part one solution
    part1slightrewrite.py:  part1 with some slight optimizations
    part2.py:               the script I used to brute-force answers for smaller numbers of steps
    part2part2.py:          the script I used to observe patterns between the numbers I got from part2.py
    part2part2attempt2.py:  the file where I did the final math to get the answer to part two
    part2rewrite.py:        a rewrite of part two based on this file's description given of my solution
                                (go there if you want any hope of understanding my code)
    README.txt:             this file
    sample.txt:             the sample input

----------------------------------------------------------------------------------------------------------------

FINAL NOTE:
I used the word "crustables" in my code a lot. I don't remember why.