from tethys_sdk.base import TethysAppBase, url_map_maker


class DamInventory(TethysAppBase):
    """
    Tethys app class for All about me.
    """

    name = 'All about me'
    index = 'dam_inventory:home'
    icon = 'dam_inventory/images/icon.gif'
    package = 'dam_inventory'
    root_url = 'dam-inventory'
    color = '#75be72'
    description = 'This is my first app'
    tags = '"Information"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)
        
        url_maps = (
            UrlMap(
                name='add_dam',
                url='dam-inventory/dams/add',
                controller='dam_inventory.controllers.add_dam'
            ),
            UrlMap(
                name='home',
                url='dam-inventory',
                controller='dam_inventory.controllers.home'
            ),
        )

        return url_maps
    
    
