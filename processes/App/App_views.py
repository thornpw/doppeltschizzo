import ablauf

# Views
# =============================================================================
# <ab> start id:menu
# menu view
# =============================================================================
class menuView(ablauf.View):
    def __init__(self, name, model):
        ablauf.View.__init__(self, name, model)

        self.rendered = False
        pass

    # <ab> start container id: menu_dialog
    def render_menu_dialog(self, segment):
        ablauf.pygamekern.filled_rectangle(segment.x, segment.y, ablauf.Data.configuration["width"], ablauf.Data.configuration["height"], (0, 0, 0))

        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        ablauf.pygamekern.scalable_text(segment.name, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: menu_dialog

    # <ab> start container id: start
    def render_start(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: start

    # <ab> start container id: options
    def render_options(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: options

    # <ab> start container id: credits
    def render_credits(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: credits

    # <ab> start container id: players
    def render_players(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: players

    # <ab> start container id: highscore
    def render_highscore(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: highscore

    # <ab> start container id: quit
    def render_quit(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: quit

    # <ab> next container id:menu

# <ab> end id: menu


# <ab> start id:options
# options view
# =============================================================================
class optionsView(ablauf.View):
    def __init__(self, name, model):
        ablauf.View.__init__(self, name, model)

        self.rendered = False
        pass

    # <ab> start container id: options_dialog
    def render_options_dialog(self, segment):
        ablauf.pygamekern.filled_rectangle(segment.x, segment.y, ablauf.Data.configuration["width"], ablauf.Data.configuration["height"], (0, 0, 0))

        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        ablauf.pygamekern.scalable_text(segment.name, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: options_dialog

    # <ab> start container id: lives
    def render_lives(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        ablauf.pygamekern.scalable_text(segment.name, segment.x, segment.y, None, 20, _color)
        ablauf.pygamekern.scalable_text(str(ablauf.Data.session["parameters"][segment.model["parameter"]]), segment.x + segment.model["parameter_x"], segment.x + segment.model["parameter_y"], None, 20, _color)

    # <ab> end container id: lives

    # <ab> start container id: exit
    def render_exit(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: exit

    # <ab> next container id:options

# <ab> end id: options


# <ab> start id:credits
# credits view
# =============================================================================
class creditsView(ablauf.View):
    def __init__(self, name, model):
        ablauf.View.__init__(self, name, model)

        self.rendered = False
        pass

    # <ab> start container id: credits_dialog
    def render_credits_dialog(self, segment):
        ablauf.pygamekern.filled_rectangle(segment.x, segment.y, ablauf.Data.configuration["width"], ablauf.Data.configuration["height"], (0, 0, 0))

        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        ablauf.pygamekern.scalable_text(segment.name, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: credits_dialog

    # <ab> start container id: exit
    def render_exit(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: exit

    # <ab> next container id:credits

# <ab> end id: credits


# <ab> start id:players
# players view
# =============================================================================
class playersView(ablauf.View):
    def __init__(self, name, model):
        ablauf.View.__init__(self, name, model)

        self.rendered = False
        pass

    # <ab> start container id: players_dialog
    def render_players_dialog(self, segment):
        ablauf.pygamekern.filled_rectangle(segment.x, segment.y, ablauf.Data.configuration["width"], ablauf.Data.configuration["height"], (0, 0, 0))

        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        ablauf.pygamekern.scalable_text(segment.name, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: players_dialog

    # <ab> start container id: player1
    def render_player1(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player1

    # <ab> start container id: player2
    def render_player2(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player2

    # <ab> start container id: player3
    def render_player3(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player3

    # <ab> start container id: player4
    def render_player4(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player4

    # <ab> start container id: player5
    def render_player5(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player5

    # <ab> start container id: player6
    def render_player6(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player6

    # <ab> start container id: player7
    def render_player7(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player7

    # <ab> start container id: player8
    def render_player8(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: player8

    # <ab> start container id: exit
    def render_exit(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: exit

    # <ab> next container id:players

# <ab> end id: players


# <ab> start id:playername
# playername view
# =============================================================================
class playernameView(ablauf.View):
    def __init__(self, name, model):
        ablauf.View.__init__(self, name, model)

        self.rendered = False
        pass

    # <ab> start container id: playername_dialog
    def render_playername_dialog(self, segment):
        ablauf.pygamekern.filled_rectangle(segment.x, segment.y, ablauf.Data.configuration["width"], ablauf.Data.configuration["height"], (0, 0, 0))

        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        ablauf.pygamekern.scalable_text(segment.name, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playername_dialog

    # <ab> start container id: playernumber
    def render_playernumber(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernumber

    # <ab> start container id: oldname
    def render_oldname(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: oldname

    # <ab> start container id: newname
    def render_newname(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: newname

    # <ab> start container id: playernamechar1
    def render_playernamechar1(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar1

    # <ab> start container id: playernamechar2
    def render_playernamechar2(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar2

    # <ab> start container id: playernamechar3
    def render_playernamechar3(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar3

    # <ab> start container id: playernamechar4
    def render_playernamechar4(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar4

    # <ab> start container id: playernamechar5
    def render_playernamechar5(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar5

    # <ab> start container id: playernamechar6
    def render_playernamechar6(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar6

    # <ab> start container id: playernamechar7
    def render_playernamechar7(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar7

    # <ab> start container id: playernamechar8
    def render_playernamechar8(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar8

    # <ab> start container id: playernamechar9
    def render_playernamechar9(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar9

    # <ab> start container id: playernamechar10
    def render_playernamechar10(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar10

    # <ab> start container id: playernamechar11
    def render_playernamechar11(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar11

    # <ab> start container id: playernamechar12
    def render_playernamechar12(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar12

    # <ab> start container id: playernamechar13
    def render_playernamechar13(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar13

    # <ab> start container id: playernamechar14
    def render_playernamechar14(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar14

    # <ab> start container id: playernamechar15
    def render_playernamechar15(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar15

    # <ab> start container id: playernamechar16
    def render_playernamechar16(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar16

    # <ab> start container id: playernamechar17
    def render_playernamechar17(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar17

    # <ab> start container id: playernamechar18
    def render_playernamechar18(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar18

    # <ab> start container id: playernamechar19
    def render_playernamechar19(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar19

    # <ab> start container id: playernamechar20
    def render_playernamechar20(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar20

    # <ab> start container id: playernamechar21
    def render_playernamechar21(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar21

    # <ab> start container id: playernamechar22
    def render_playernamechar22(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar22

    # <ab> start container id: playernamechar23
    def render_playernamechar23(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar23

    # <ab> start container id: playernamechar24
    def render_playernamechar24(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar24

    # <ab> start container id: playernamechar25
    def render_playernamechar25(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar25

    # <ab> start container id: playernamechar26
    def render_playernamechar26(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar26

    # <ab> start container id: playernamechar27
    def render_playernamechar27(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar27

    # <ab> start container id: playernamechar28
    def render_playernamechar28(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar28

    # <ab> start container id: playernamechar29
    def render_playernamechar29(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar29

    # <ab> start container id: playernamechar30
    def render_playernamechar30(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar30

    # <ab> start container id: playernamechar31
    def render_playernamechar31(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar31

    # <ab> start container id: playernamechar32
    def render_playernamechar32(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar32

    # <ab> start container id: playernamechar33
    def render_playernamechar33(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar33

    # <ab> start container id: playernamechar34
    def render_playernamechar34(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar34

    # <ab> start container id: playernamechar35
    def render_playernamechar35(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar35

    # <ab> start container id: playernamechar36
    def render_playernamechar36(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar36

    # <ab> start container id: playernamechar37
    def render_playernamechar37(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar37

    # <ab> start container id: playernamechar38
    def render_playernamechar38(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar38

    # <ab> start container id: playernamechar39
    def render_playernamechar39(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar39

    # <ab> start container id: playernamechar40
    def render_playernamechar40(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: playernamechar40

    # <ab> start container id: backspace
    def render_backspace(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: backspace

    # <ab> start container id: exit
    def render_exit(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: exit

    # <ab> start container id: ok
    def render_ok(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: ok

    # <ab> next container id:playername

# <ab> end id: playername


# <ab> start id:highscore
# highscore view
# =============================================================================
class highscoreView(ablauf.View):
    def __init__(self, name, model):
        ablauf.View.__init__(self, name, model)

        self.rendered = False
        pass

    # <ab> start container id: highscore_dialog
    def render_highscore_dialog(self, segment):
        ablauf.pygamekern.filled_rectangle(segment.x, segment.y, ablauf.Data.configuration["width"], ablauf.Data.configuration["height"], (0, 0, 0))

        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        ablauf.pygamekern.scalable_text(segment.name, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: highscore_dialog

    # <ab> start container id: tournament
    def render_tournament(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        #data
        xpositions_data = segment.model["x_data"]
        xpositions_data = xpositions_data.split("|")

        # header
        xpositions_header = segment.model["x_header"]
        xpositions_header = xpositions_header.split("|")

        _counter = 0
        for _header_part in segment.model["header"].split("|"):
            ablauf.pygamekern.scalable_text(_header_part, int(xpositions_header[_counter]), segment.model["y_header"], None, 20, _color)
            _counter += 1

        if ("sort_column" in segment.model) and ("reverse" in segment.model):
            #_sorted = sorted( ablauf.Data.session[segment.model['data']], key=lambda score: int(score[segment.model['sort_column']]), reverse=True )
            _sorted = sorted( ablauf.Data.session[segment.model['data']], key=lambda score: int(score[segment.model['sort_column']]), reverse=segment.model['reverse'])
        else:
            _sorted =  ablauf.Data.session[segment.model['data']]

        # data
        _row_counter = 0
        for _row in _sorted:
            _column_counter = 0
            for _column in segment.model['columns'].split("|"):
                ablauf.pygamekern.scalable_text(str(_row[_column]), int(xpositions_data[_column_counter]), segment.model["y_data"] + (_row_counter * segment.model["y_offset"]), None, 20, _color)
                _column_counter += 1
            _row_counter += 1

    # <ab> end container id: tournament

    # <ab> start container id: scores
    def render_scores(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        #data
        xpositions_data = segment.model["x_data"]
        xpositions_data = xpositions_data.split("|")

        # header
        xpositions_header = segment.model["x_header"]
        xpositions_header = xpositions_header.split("|")

        _counter = 0
        for _header_part in segment.model["header"].split("|"):
            ablauf.pygamekern.scalable_text(_header_part, int(xpositions_header[_counter]), segment.model["y_header"], None, 20, _color)
            _counter += 1

        if ("sort_column" in segment.model) and ("reverse" in segment.model):
            #_sorted = sorted( ablauf.Data.session[segment.model['data']], key=lambda score: int(score[segment.model['sort_column']]), reverse=True )
            _sorted = sorted( ablauf.Data.session[segment.model['data']], key=lambda score: int(score[segment.model['sort_column']]), reverse=segment.model['reverse'])
        else:
            _sorted =  ablauf.Data.session[segment.model['data']]

        # data
        _row_counter = 0
        for _row in _sorted:
            _column_counter = 0
            for _column in segment.model['columns'].split("|"):
                ablauf.pygamekern.scalable_text(str(_row[_column]), int(xpositions_data[_column_counter]), segment.model["y_data"] + (_row_counter * segment.model["y_offset"]), None, 20, _color)
                _column_counter += 1
            _row_counter += 1

    # <ab> end container id: scores

    # <ab> start container id: exit
    def render_exit(self, segment):
        if segment.key == self.model.actual_path:
            _color = self.model.color_selected
        else:
            _color = self.model.color_text

        if "text" in segment.model:
            _session_data = ""
            if "data" in segment.model:
                for _element in segment.model["data"]:
                    _session_data += "ablauf.Data.session" + _element +","
                _session_data = _session_data[:-1]

            exec("_text = '{0}'.format({1})".format(segment.model["text"],_session_data))
        else:
            _text = segment.name

        ablauf.pygamekern.scalable_text(_text, segment.x, segment.y, None, 20, _color)

    # <ab> end container id: exit

    # <ab> next container id:highscore

# <ab> end id: highscore

