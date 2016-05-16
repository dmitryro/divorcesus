// import external dependencies
// docs component handles routing and demo pages
import {vsDocsPages, vsDocsDrawer} from 'vuestrap-docs/src/components'

// drawer
import {offcanvasWrapper as vsOffcanvasWrapper, offcanvasDrawer as vsOffcanvasDrawer} from 'src/components/offcanvas-drawer'
import vsToast from 'src/components/toast'

// import utils
import {getRoutes} from 'vuestrap-docs/src/utils'

// import routes from all docs
import docsRoutes from 'src/docs'

// import package.json meta data
import pkg from 'package.json'

// get list of the route objects
const routes = getRoutes(docsRoutes)

// create components from routes and attach it to the docs.components object
routes.forEach((route) => {
	vsDocsPages.components[route.id] = route.component
})

// start docs instance
window.docs = new Vue({
	el: '#docs',
	data: {
		routes: routes,
		pageTitle: 'Vuestrap Docs',
		animation: 'ease',
    animations: [
      { text: 'none', value: 'none' },
      { text: 'ease', value: 'ease' },
      { text: 'linear', value: 'linear' },
      { text: 'ease-in', value: 'ease-in' },
      { text: 'ease-out', value: 'ease-out' },
      { text: 'ease-in-out', value: 'ease-in-out' },
      { text: 'bounce', value: 'bounce' },
      { text: 'snappy', value: 'snappy' },
      { text: 'out-of-orbit', value: 'out-of-orbit' },
    ],
    align: 'right',
    aligns: [{text: 'left', value: 'left'}, {text: 'right', value: 'right'}],
    pkg: pkg,
	},
	methods: {
    closeDropdownsAndPopovers() {
      this.$broadcast('hide::popover')
      this.$broadcast('hide::tooltip')
      this.$broadcast('hide::dropdown')
      this.console = ''
    },
  },
	components: {
		vsDocsPages,
    vsDocsDrawer,
		vsOffcanvasWrapper,
		vsOffcanvasDrawer,
    vsToast,
	},
})

