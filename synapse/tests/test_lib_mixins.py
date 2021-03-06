from synapse.tests.common import *

import synapse.lib.mixins as s_mixins

class Foo: pass
class Bar: pass

class MixTest(SynTest):
    def test_lib_mixins_basics(self):
        s_mixins.addSynMixin('ut', 'synapse.tests.test_lib_mixins.Foo')
        s_mixins.addSynMixin('ut', 'synapse.tests.test_lib_mixins.Baz', 'synapse.tests.test_lib_mixins.Bar')
        self.eq(s_mixins.getSynMixins('ut', 'synapse.tests.test_lib_mixins.Foo')[0], Foo)
        self.eq(s_mixins.getSynMixins('ut', 'synapse.tests.test_lib_mixins.Baz')[0], Bar)
