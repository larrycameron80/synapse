import regex

import synapse.lib.cmdr as s_cmdr
import synapse.cmds.cortex as s_cmds_cortex

from synapse.tests.common import *

class SynCmdCommonTest(SynTest):

    def test_cmds_help(self):
        with self.getDmonCore() as core:
            outp = self.getTestOutp()
            cmdr = s_cmdr.getItemCmdr(core, outp=outp)
            cmdr.runCmdLine('help')
            self.true(outp.expect('List commands and display help output.'))

            cmdr.runCmdLine('help quit')
            self.true(outp.expect('Quit the current command line interpreter.'))

            cmdr.runCmdLine('help notacommand')
            self.true(outp.expect('=== NOT FOUND: notacommand'))

    def test_cmds_quit(self):
        with self.getDmonCore() as core:
            outp = self.getTestOutp()
            cmdr = s_cmdr.getItemCmdr(core, outp=outp)
            cmdr.runCmdLine('quit')
            self.true(outp.expect('o/'))

    def test_cmds_guid(self):
        with self.getDmonCore() as core:
            outp = self.getTestOutp()
            cmdr = s_cmdr.getItemCmdr(core, outp=outp)
            cmdr.runCmdLine('guid')
            self.true(outp.expect('new guid:'))
