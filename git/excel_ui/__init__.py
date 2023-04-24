import os
import sys

from past.builtins import execfile

if self.action is not None:
    # print self.action
    # print self.selected_ids
    self.executeAction(self.action, self.selected_ids)

# ----------------------------------------------
# Call Action
# ----------------------------------------------
def executeAction(self, sg_action, id_list):
    try:
        SG_AMI_ROOT = os.path.dirname(__file__)
        SG_AMI_PLUGIN_PATH = SG_AMI_ROOT + "/plugins"
        sg_action_path = SG_AMI_PLUGIN_PATH + "/%s.py" % sg_action
        if os.path.exists(sg_action_path):
            #args = [str(sg_action_path), str(id_list)]
            sys.argv = [sg_action_path, id_list]
            print("SG_ACTION_PATH: %s" % (str(sg_action_path)))
            output = execfile(sg_action_path)
            if output is not None:
                print()
                var = "SG_ACTION %s Reported Output: \n %s" % (sg_action, output)
                time.sleep(120)
    except Exception:
        print "Execute %s Reported Errors: \n %s" % (sg_action_path, str(traceback.format_exc()))
        time.sleep(120)