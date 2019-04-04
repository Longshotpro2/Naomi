# -*- coding: utf-8 -*-
"""
These functions "walk" the profile, and return either a boolean variable to
tell whether an option is configured or not, or the actual value
"""
from naomi import paths
import os
import yaml

_profile = {}
_profile_read = False
_test_profile = False


def set_profile(custom_profile):
    """
    Set the profile to a custom value. This is especially helpful when testing
    """
    global _profile, _profile_read, _test_profile
    _profile = custom_profile
    _test_profile = True
    _profile_read = True


def get_profile(command=""):
    global _profile, _profile_read, _test_profile
    command = command.strip().lower()
    if command == "reload":
        _profile_read = False
    elif command != "":
        raise ValueError("command '{}' not understood".format(command))
    if not _profile_read:
        # Open and read the profile
        configfile = paths.config('profile.yml')
        with open(configfile, "r") as f:
            _profile = yaml.safe_load(f)
        _profile_read = True
        _test_profile = False
    return _profile


def save_profile():
    global _profile, _profile_read, _test_profile
    # I want to make sure the user's profile is never accidentally overwritten
    # with a test profile.
    if not _test_profile:
        # Save the profile
        if not os.path.exists(paths.CONFIG_PATH):
            os.makedirs(paths.CONFIG_PATH)
        outputFile = open(paths.config("profile.yml"), "w")
        yaml.dump(get_profile(), outputFile, default_flow_style=False)


def get_profile_var(path, default=None):
    """
    Get a value from the profile, whether it exists or not
    If the value does not exist in the profile, returns
    either the default value (if there is one) or None.
    """
    response = _walk_profile(path, True)
    if response is None:
        response = default
    return response


def get_profile_flag(path, default=None):
    """
    Get a boolean value from the profile, whether it exists
    or not. If the value does not exist, returns default or
    None
    """
    # Get the variable value
    temp = str(_walk_profile(path, True))
    if(temp is None):
        # the variable is not defined
        temp = default
    response = False
    if str(temp).strip().lower() in ('true', 'yes', 'on'):
        response = True
    return response


def check_profile_var_exists(path):
    """
    Checks if an option exists in the test_profile it is using.
    Option is passed in as a list so that if we need to check
    if a suboption exists, we can pass the full path to it.
    """
    return _walk_profile(path, False)


def _walk_profile(path, returnValue):
    """
    Function to walk the profile
    """
    profile = get_profile()
    found = True
    for branch in path:
        try:
            profile = profile[branch]
        except KeyError:
            found = False
            profile = None
            break
    if(returnValue):
        response = profile
    else:
        response = found
    return response


def set_profile_var(path, value):
    global _profile
    temp = _profile
    if len(path) > 0:
        last = path[0]
        if len(path) > 1:
            for branch in path[1:]:
                try:
                    if not isinstance(temp[last], dict):
                        temp[last] = {}
                except KeyError:
                    temp[last] = {}
                temp = temp[last]
                last = branch
        temp[last] = value
    else:
        raise KeyError("Can't write to profile root")