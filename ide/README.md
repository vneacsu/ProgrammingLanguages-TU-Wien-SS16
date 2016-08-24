# Prerequisites
    
1. Install haskell-stack
2. Install ncurses (AUR packages)
3. cd /usr/include && mkdir ncursesw && ln /usr/include/ncurses.h /usr/include/ncursesw/ && /usr/include/panel.h /usr/include/ncursesw/
4. Run stack setup
    
# Build and Run
    stack build
    stack exec ide [<path to file to open in editor>]