"""
This handle the plot using bokeh.
"""

import os.path
import gettext
import bokeh.models.formatters
import bokeh.plotting as plt
from . import prof

THIS_DIR, THIS_FILENAME = os.path.split(__file__)
THIS_TRANSLATION = gettext.translation('perprof',
        os.path.join(THIS_DIR, 'locale'))
_ = THIS_TRANSLATION.gettext

# TODO: Add more colors to list and compatible with others backend
BOKEH_COLOR_LIST = ["blue",
                    "green",
                    "red",
                    "cyan",
                    "magenta",
                    "yellow"]

class Profiler(prof.Pdata):
    """
    The profiler using bokeh
    """
    def __init__(self, parser_options, profiler_options):
        """
        :param dict parser_options: parser options
        :param dict profiler_options: profiler options
        """
        if profiler_options['output'] is None:
            self.output = 'performance-profile.{}'.format(
                    profiler_options['output_format'])
        else:
            self.output = '{}.{}'.format(profiler_options['output'],
                    profiler_options['output_format'])
        self.output_format = profiler_options['output_format']

        # Language for the axis label
        translation = gettext.translation('perprof',
                os.path.join(THIS_DIR, 'locale'), [profiler_options['lang']])
        self.axis_lang = translation.gettext

        prof.Pdata.__init__(self, parser_options, profiler_options)

    def plot(self):
        """
        Create the performance profile using matplotlib.
        """
        if not self.force:
            try:
                file_ = open(self.output, 'r')
                file_.close()
                raise ValueError(_('ERROR: File {} exists.\nUse `-f` to overwrite').format(self.output))
            except FileNotFoundError:
                pass

        if not self.already_scaled:
            self.scale()

        try:
            self.ppsbt
        except AttributeError:
            self.set_percent_problems_solved_by_time()

        plt.output_file(self.output, title="")

        # Axis
        try:
            maxt = min(max(self.times), self.tau)
        except (AttributeError, TypeError):
            maxt = max(self.times)

        boken_plot_options = {"x_range":[1,maxt], "y_range":[0,1]}

        # Change the xscale to log scale
        if self.semilog:
            boken_plot_options["x_axis_type"] = "log"

        p = plt.figure(title="",
                x_axis_label=self.axis_lang('Performance Ratio'),
                y_axis_label=self.axis_lang('Problems solved'),
                **boken_plot_options)

        for idx, solver in enumerate(self.solvers):
            p.line(self.times,
                    self.ppsbt[solver],
                    legend=solver,
                    line_width=2,
                    line_color=BOKEH_COLOR_LIST[idx % len(BOKEH_COLOR_LIST)])

        # Legend
        p.legend.orientation = "bottom_right"

        # Help lines
        p.grid.grid_line_color = "black"
        p.grid.grid_line_alpha = 0.5

        # Save the plot
        plt.save(p)
