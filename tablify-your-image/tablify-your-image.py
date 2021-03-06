#!/usr/bin/env python2
# -*- coding: utf8 -*-

from PIL import Image
import os
import sys
import argparse

def main(argv):
    __version__ = "0.4.0"
    
    # Path to the image
    path = ""

    # A variable to store the string that we are going to create
    table = ""
    
    # Create a parser to parse the arguments
    parser = argparse.ArgumentParser()
    
    # Optional arguments
    parser.add_argument("-v", "--version", help="print the version number and exit", action='version', version='%(prog)s ' + __version__)
    parser.add_argument("-s", "--stdout", help="print the html to the standard output", action='store_true')
    parser.add_argument("-x", "--width", type=int, default=1, help="the width of each td in pixels (default = 1)")
    parser.add_argument("-y", "--height", type=int, default=1, help="the height of each td in pixels (default = 1)")
    parser.add_argument("-o", "--output", help="the path to the output file. If omitted, the name of the input file is used. It doesn't work when the --stdout option is specified.")
    parser.add_argument("-d", "--id", help="the id of the table")
    
    # Positional arguments
    parser.add_argument("input", help="the path to the file that you want to tablify")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # If the user set a value for the --input argument
    if args.input:
        path = args.input
    
    if args.output:
        # Use the name supplied by the user as the name of the new html file.
        name = args.output
    else:
        # Get the name of the image from the path -> we are going to use it as the name of the new html file
        name = os.path.splitext(os.path.basename(path))[0] + '.html'
    
    id_table = ""
    
    # If the user supplied a id, use it to construct the id attribute of the table.
    if args.id:
        id_table = 'id="' + args.id + '" '
    
    # Open the image
    im = Image.open(path)
    
    # Convert to RGBA
    rgba_im = im.convert('RGBA')
    
    # Get the width and height of the image (in pixels)
    width, height = im.size
    
    # Create the table.
    table = table + '<table ' + id_table + 'cellspacing="0" cellpadding="0" border="0" style="margin-left: auto; margin-right: auto; font-size:0px;">\n'
    
    # Create the body of the table
    table = table + '<tbody>\n'
    
    # Create a <td> for each pixel of the image with the corresponding color
    for y in range(0, height):
        for x in range(0, width):
            # If it is the first column (0st), create an tr tag
            if x == 0:
                table = table + '<tr>'
            
            # Get the color of the corresponding pixel
            r, g, b, a = rgba_im.getpixel((x, y))
            
            table = table + '<td width="' + str(args.width) + '" height="' + str(args.height) + '" colspan="1" style="background-color: ' + 'rgba(%d,%d,%d,%.1f)' % (r, g, b, a / 255.0)  + ';">&nbsp;</td>'
    
            # If it is the last column, close the tr tag
            if x == width - 1:
                table = table + '</tr>'
    
            # Add a new line
            table = table + '\n'
    
    # Close the body of the table and the table itself
    table = table + '</tbody></table>'
    
    # If the user wants to print the table to the standard output
    if args.stdout:
        print table
    else:
        # Create the html file
        f = open(name, 'w')
        
        # Write the table to the html file
        f.write(table)
        
        # Close the html file
        f.close()

if __name__ == "__main__":
   main(sys.argv[1:])