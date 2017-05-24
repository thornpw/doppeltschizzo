import ablauf
import ablauf.apmn
import steuer
from ablauf import pygamekern


# State functions
# ============================================================================
# init state
# ****************************************************************************
class Init(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        """
        Steuer initialization
        """
        ablauf.Automate.input_handler.Action('DPAD_TOP', 1, 'DPad top', 'DT', 52, 90, 42, 40)
        ablauf.Automate.input_handler.Action('DPAD_DOWN', 2, 'DPad down', 'DD', 52, 149, 42, 40)
        ablauf.Automate.input_handler.Action('DPAD_LEFT', 4, 'DPad left', 'DL', 11, 120, 42, 40)
        ablauf.Automate.input_handler.Action('DPAD_RIGHT', 8, 'DPad right', 'DR', 94, 119, 42, 40)
        ablauf.Automate.input_handler.Action('BUTTON_TOP', 4096, 'Button top', 'BT', 306, 90, 42, 40)
        ablauf.Automate.input_handler.Action('BUTTON_DOWN', 8192, 'Button down', 'BD', 306, 149, 42, 40)
        ablauf.Automate.input_handler.Action('BUTTON_LEFT', 16384, 'Button left', 'BL', 264, 120, 42, 40)
        ablauf.Automate.input_handler.Action('BUTTON_RIGHT', 32768, 'Button right', 'BR', 347, 119, 42, 40)
        ablauf.Automate.input_handler.Action('SHOULDER_L1', 65535, 'Shoulder L1', 'L1', 52, 36, 42, 26)
        ablauf.Automate.input_handler.Action('SHOULDER_L2', 131072, 'Shoulder L2', 'L2', 52, 10, 42, 26)
        ablauf.Automate.input_handler.Action('SHOULDER_R1', 262144, 'Shoulder R1', 'R1', 306, 36, 42, 26)
        ablauf.Automate.input_handler.Action('SHOULDER_R2', 524288, 'Shoulder R2', 'R2', 306, 10, 42, 26)
        ablauf.Automate.input_handler.Action('ANALOG_L3', 1048576, 'Analog L3', 'L3', 112, 192, 54, 54)
        ablauf.Automate.input_handler.Action('ANALOG_R3', 2097152, 'Analog R3', 'R3', 232, 192, 54, 54)
        ablauf.Automate.input_handler.Action('BUTTON_START', 4194304, 'Button start', 'ST', 215, 119, 37, 26)
        ablauf.Automate.input_handler.Action('BUTTON_SELECT', 8388608, 'Button select', 'SE', 147, 119, 37, 26)
        ablauf.Automate.input_handler.Action('LEFT_TOP', 16777216, 'Left analog stick top', 'LT', 112, 142, 54, 54)
        ablauf.Automate.input_handler.Action('LEFT_DOWN', 33554432, 'Left analog stick down', 'LD',112, 242, 54, 54)
        ablauf.Automate.input_handler.Action('LEFT_LEFT', 67108864, 'Left analog stick left', 'LL', 62, 192, 54, 54)
        ablauf.Automate.input_handler.Action('LEFT_RIGHT', 134217728, 'Left analog stick right', 'LR', 162, 192, 54, 54)
        ablauf.Automate.input_handler.Action('RIGHT_TOP', 268435456, 'Right analog stick top', 'RT', 232, 142, 54, 54)
        ablauf.Automate.input_handler.Action('RIGHT_DOWN', 536870912, 'Right analog stick down', 'RD', 232, 242, 54, 54)
        ablauf.Automate.input_handler.Action('RIGHT_LEFT', 1073741824, 'Right analog stick left', 'RL', 182, 192, 54, 54)
        ablauf.Automate.input_handler.Action('RIGHT_RIGHT', 2147483648, 'Right analog stick right', 'RR', 282, 192, 54, 54)

        # Set direction callback functions
        ablauf.Automate.input_handler.Direction('DPAD_TOP', 0b0001, 'DPad top', 'Top', None, None)
        ablauf.Automate.input_handler.Direction('DPAD_DOWN', 0b0010, 'DPad down', 'Down', None, None)
        ablauf.Automate.input_handler.Direction('DPAD_LEFT', 0b0100, 'DPad left', 'Left', None, None)
        ablauf.Automate.input_handler.Direction('DPAD_RIGHT', 0b1000, 'DPad right', 'Right', None, None)
        ablauf.Automate.input_handler.Direction('DPAD_TOPLEFT', 0b0101, 'DPad top', 'Top Left', None, None)
        ablauf.Automate.input_handler.Direction('DPAD_TOPRIGHT', 0b1001, 'DPad down', 'Down Right', None, None)
        ablauf.Automate.input_handler.Direction('DPAD_DOWNLEFT', 0b0110, 'DPad down left', 'Down Left', None, None)
        ablauf.Automate.input_handler.Direction('DPAD_DOWNRIGHT', 0b1010, 'DPad down right', 'Down Right', None, None)

        steuer.init(use_events=False)


# init_wait state
# ****************************************************************************
class InitWait(ablauf.apmn.Wait):
    def __init__(self, config):
        ablauf.apmn.Wait.__init__(self, config)


# detect_connected_controllers state
# ****************************************************************************
class DetectConnectedControllers(ablauf.apmn.MultiInstance):
    def __init__(self, config):
        ablauf.apmn.MultiInstance.__init__(self, config)

    def iteration(self):
        return steuer.controllers


# exist_controller_type state
# ****************************************************************************
class ExistControllerType(ablauf.apmn.ExclusiveGateway):
    def __init__(self, config):
        ablauf.apmn.ExclusiveGateway.__init__(self, config)

    def test(self):
        return ablauf.Data.session['database_mapping'] is None

    def enter_state(self):
        ablauf.Data.session['database_mapping'] = steuer.get_mapping_by_controller(ablauf.Data.session['DetectConnectedControllers_element'])

    def transition_to_OnControllerTypeNotFound_yes(self):
        steuer.Configuration.mark_as_undetected(ablauf.Data.session['DetectConnectedControllers_element'])

    def transition_to_OnControllerDetected_no(self):
        ablauf.Data.session['DetectConnectedControllers_element'].set_mapping(ablauf.Data.session['database_mapping'])


# exist_undetected_controllers state
# ****************************************************************************
class ExistUndetectedControllers(ablauf.apmn.ExclusiveGateway):
    def __init__(self, config):
        ablauf.apmn.ExclusiveGateway.__init__(self, config)

    def test(self):
        return steuer.Configuration.undetected_controllers


# explain_unknown_wait state
# ****************************************************************************
class ExplainUnknownWait(ablauf.apmn.Wait):
    def __init__(self, config):
        ablauf.apmn.Wait.__init__(self, config)


# iterate_unmapped_controllers state
# ****************************************************************************
class IterateUnmappedControllers(ablauf.apmn.MultiInstance):
    def __init__(self, config):
        ablauf.apmn.MultiInstance.__init__(self, config)

    def iteration(self):
        return steuer.Configuration.undetected_controllers

    def enter_state(self):
        steuer.Configuration.init_undetected_controller_configuration()

    def leave_state(self):
        steuer.Configuration.exit_undetected_controller_configuration()


# exist_mapping state
# ****************************************************************************
class ExistMapping(ablauf.apmn.ExclusiveGateway):
    def __init__(self, config):
        ablauf.apmn.ExclusiveGateway.__init__(self, config)

    def test(self):
        return ablauf.Data.session["mapping"] is not None

    def enter_state(self):
        ablauf.Data.session["mapping"] = steuer.Configuration.get_mapping_if_already_configured(ablauf.Data.session["IterateUnmappedControllers_element"])


# iterate_unconfigured_actions state
# ****************************************************************************
class IterateUnconfiguredActions(ablauf.apmn.MultiInstance):
    def __init__(self, config):
        ablauf.apmn.MultiInstance.__init__(self, config)

    def iteration(self):
        return steuer.Action.unconfigured_actions

    def enter_state(self):
        steuer.Configuration.init_mapping(ablauf.Data.session["IterateUnmappedControllers_element"])

    def transition_to_OnControllerTypeMappingFinished_exit(self):
        steuer.Configuration.exit_mapping(ablauf.Data.session['IterateUnmappedControllers_element'])


# detect_event state
# ****************************************************************************
class DetectEvent(ablauf.apmn.Loop):
    def __init__(self, config):
        ablauf.apmn.Loop.__init__(self, config)

    def test(self):
        return ablauf.Data.session["IterateUnconfiguredActions_element"].status == steuer.Action.status_waiting

    def task(self):
        ablauf.Data.session["IterateUnconfiguredActions_element"].detect_event(ablauf.Data.session["IterateUnmappedControllers_element"], ablauf.Data.session["actual_event"])

    def enter_state(self):
        ablauf.Data.session['IterateUnconfiguredActions_element'].init_event_detection(ablauf.Data.session['IterateUnmappedControllers_element'])


# wait_for_trigger_release state
# ****************************************************************************
class WaitForTriggerRelease(ablauf.apmn.Loop):
    def __init__(self, config):
        ablauf.apmn.Loop.__init__(self, config)

    def test(self):
        return ablauf.Data.session["IterateUnconfiguredActions_element"].status == steuer.Action.status_test_remapping

    def task(self):
        ablauf.Data.session["IterateUnconfiguredActions_element"].wait_for_trigger_release(ablauf.Data.session["actual_event"])


# is_event_unmapped state
# ****************************************************************************
class IsEventUnmapped(ablauf.apmn.ExclusiveGateway):
    def __init__(self, config):
        ablauf.apmn.ExclusiveGateway.__init__(self, config)

    def test(self):
        return ablauf.Data.session["IterateUnconfiguredActions_element"].is_event_unmapped(ablauf.Data.session["IterateUnmappedControllers_element"])

    def transition_to_OnEventMapped_yes(self):
        ablauf.Data.session["IterateUnconfiguredActions_element"].map_event(ablauf.Data.session["IterateUnmappedControllers_element"])


# delay_mapping state
# ****************************************************************************
class DelayMapping(ablauf.apmn.MultiInstance):
    def __init__(self, config):
        ablauf.apmn.MultiInstance.__init__(self, config)

    def iteration(self):
        return iter([1, 2, 3, 4, 5,6])

    def task(self):
        ablauf.Data.session["IterateUnconfiguredActions_element"].delay_mapping(ablauf.Data.session["IterateUnmappedControllers_element"])


# delay_mapping_wait state
# ****************************************************************************
class DelayMappingWait(ablauf.apmn.Wait):
    def __init__(self, config):
        ablauf.apmn.Wait.__init__(self, config)


# ExitWait state
# ****************************************************************************
class ExitWait(ablauf.apmn.Wait):
    def __init__(self, config):
        ablauf.apmn.Wait.__init__(self, config)


# set_mapping state
# ****************************************************************************
class SetMapping(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        ablauf.Data.session["IterateUnmappedControllers_element"].set_mapping(ablauf.Data.session["mapping"])


# map_event_to_action state
# ****************************************************************************


# hooks
# =============================================================================
class OnControllerDetected(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        pass


class OnInitialized(ablauf.apmn.UserTask):
    def __init__(self, config):
        ablauf.apmn.UserTask.__init__(self, config)

    def task(self):
        ablauf.logger.info("EVENT:" + "Steuer initialized")
        ablauf.logger.info("----------- Initialization -------")
        if steuer.mapping_databases['default'].found_database:
            ablauf.logger.info("Steuer mapping database found and loaded")

            ablauf.Data.session["stema_status"] = ablauf.Data.translations["mapping_database_found_and_loaded"]
            ablauf.Data.session["mapping_database_status"] = True
        else:
            ablauf.logger.info("No mapping database found. A new one will be created")

            ablauf.Data.session["stema_status"] = ablauf.Data.translations["no_mapping_database_found_a_new_one_will_be_created"]
            ablauf.Data.session["mapping_database_status"] = False

        ablauf.Automate.actual_process.actual_state.exit = True


# Detection events
# ****************************************************************************
class OnDetectionFinished(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        ablauf.logger.info("EVENT:" + "controller detection finished")
        ablauf.logger.info("----------- Detection ------------")
        ablauf.logger.info("{0} controllers found".format(steuer.controllers.__len__()))

        ablauf.Data.session["number_of_controllers"] = steuer.controllers.__len__()

        for controller in steuer.controllers:
            if controller.is_mapped:
                ablauf.logger.info("controller {0}:{1} was found in the mapping database and its events are mapped to actions".format(controller.number, controller.name))
            else:
                ablauf.logger.info("controller {0}:{1} was not found in mapping database".format(controller.number, controller.name))

            ablauf.Data.session["controllers_status"].append(0)


class OnMappingFinished(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        ablauf.logger.info("EVENT:" + "mapping finished")


# Mapping events
# ****************************************************************************
class OnControllerMapped(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        controller = ablauf.Data.session['DetectConnectedControllers_element']
        ablauf.logger.info("EVENT:" + "controller {0}:{1} mapped".format(controller.number, controller.name))


class OnControllerTypeNotFound(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        controller = ablauf.Data.session['DetectConnectedControllers_element']
        ablauf.logger.info("EVENT:" + "controller {0}:{1} could not be mapped. Controller name unknown.".format(controller.number, controller.name))


# Configuration events
# ****************************************************************************
class OnStartConfiguration(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        ablauf.logger.info("EVENT:" + "Start configuration of unknown controller types")
        ablauf.Data.session["phase"] = ablauf.Data.translations["configuration"]


class OnConfigurationFinished(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        ablauf.logger.info("EVENT:" + "All controllers are configured")

# Configuration controller type events
class OnControllerTypeMappingInit(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        controller = ablauf.Data.session['IterateUnmappedControllers_element']
        ablauf.Data.session["actual_controller"] = controller
        ablauf.Data.session["controllers_status"][controller.number] = 1
        ablauf.logger.info("EVENT:" + "Start configure controller type :{0}".format(controller.name))
        ablauf.Data.session["stema_status"] = ablauf.Data.translations["start_mapping"].format(controller.name)


class OnControllerTypeMappingFinished(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        controller = ablauf.Data.session['IterateUnmappedControllers_element']
        ablauf.Data.session["mapping"] = controller.mapping
        ablauf.Data.session["controllers_status"][controller.number] = 0
        ablauf.logger.info("EVENT:" + "controller type {0} configuration finished".format(controller.name))


# Map controller type events
# ****************************************************************************
class OnRequestAction(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        """
        Callback function that is triggered, when a new action should be configured
        """
        controller = ablauf.Data.session["IterateUnmappedControllers_element"]
        action2configure = ablauf.Data.session["IterateUnconfiguredActions_element"]

        ablauf.Data.session["actual_action"] = action2configure
        ablauf.Data.session["action_status"] = ablauf.Data.translations["trigger_the_event_then_release_it"]
        ablauf.Data.session["is_waiting"] = False

        ablauf.logger.info("EVENT:" + "Controller " + str(controller.number) + ": " + action2configure.long_name)


class OnEventMapped(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        controller = ablauf.Data.session["DetectConnectedControllers_element"]
        action2configure = ablauf.Data.session["IterateUnconfiguredActions_element"]
        ablauf.logger.info("EVENT:" + "Controller {0}:{1} - action:{2} mapped".format(controller.number, controller.name, action2configure.action))
        ablauf.Data.session["stema_status"] = ablauf.Data.translations["action_mapped"].format(action2configure.long_name)


class OnEventAlreadyMapped(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        controller = ablauf.Data.session["IterateUnmappedControllers_element"]
        action2configure = ablauf.Data.session["IterateUnconfiguredActions_element"]
        ablauf.logger.info("EVENT:" + "Error: Controller {0}:{1} - action {2} already mapped".format(controller.number, controller.name, action2configure.action))
        ablauf.Data.session["stema_status"] = ablauf.Data.translations["event_was_already_mapped"]


class OnWait(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        controller = ablauf.Data.session["IterateUnmappedControllers_element"]

        ablauf.Data.session["action_status"] = ablauf.Data.translations["wait"]
        ablauf.Data.session["is_waiting"] = True
        pygamekern.Kernel.sync = True

        ablauf.logger.info("EVENT:" + "Controller {0}:{1} - is waiting".format(controller.number, controller.name))