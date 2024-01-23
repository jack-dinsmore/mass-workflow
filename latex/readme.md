# Jack's figure copying code

## Installation

1. Change `ROOT` to your research workspace and `FIGURE_DIRECTORY` to the place where you keep your figures

2. Place **.get-figs** and **.fig-list** in that same figure directory

3. If you want, change `EXTENSIONS` to be the list of image extensions you use, in order of preference.

## Use

1. List the figures you want to include, giving first the latex label you'll use, then the path to the file within your research workspace

2. Run `python .get-figs`. WARNING: this will delete all figures currently in the figure directory. If you don't want to do this, edit the code.
