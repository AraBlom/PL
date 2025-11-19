from ColorText import ColorText
from AssemblyLine import AssemblyLine

SHOW_REDIRECTED_INPUT_COMMENTS = False
LINE_MARKER = " ##############################################################"


def cleanInput( prompt ):
  result = input( prompt )
  # strips out blank lines in input
  while result == '' or result[ 0 ] == '#':
    if len( result ) > 0 and result[ 0 ] == '#' and SHOW_REDIRECTED_INPUT_COMMENTS:
      print( ColorText.fg.cyan + result + LINE_MARKER + ColorText.reset )
    result = input()
  
  return result

def main( ):
    menu = "\n" \
           "1) Add Package\n"\
           "2) Update One Tick\n"\
           "3) Update X Ticks\n"\
           "4) Make New Simulator\n"\
           "5) Set Appearance\n"\
           "0) Quit\n"\

    line = AssemblyLine()
    choice = -1
    while choice != 0:
        line.print_line()
        print( menu )
        try:
            choice = int(cleanInput( "Choice:> " ))

            if choice == 1:
                pkg_type = float (cleanInput("Type:> "))
                capacity = float(cleanInput("Max Units:> "))
                if int(pkg_type) == pkg_type and int(capacity) == capacity:
                    line.addPackage(int(pkg_type), int(capacity))
                else:
                    raise ValueError

            elif choice == 2:
                print( "TODO" )

            elif choice == 3:
                print( "TODO" )

            elif choice == 4:
                print( "TODO" )

            elif choice == 5:
                print( "TODO" )

            elif choice == 6:
                print( "TODO" )


            elif choice == 0 or choice == '0':
                choice = 0
            else:
                e = IndexError()
                e.add_note("0-5")
                raise e
        except ValueError: #GRADING: CATCH
            print("Please, input an integer")
        except IndexError as ie:
            print("Out of " + str(ie.__notes__[0]) +" range")

if __name__ == '__main__':
    main( )
