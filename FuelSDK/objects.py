from FuelSDK.rest import ET_GetSupportRest,ET_GetSupport,ET_Get

class ET_ContentArea(ET_GetSupport):    
    """
    Wrap an Exact Target Content Area.
    """
    def __init__(self):
        super(ET_ContentArea, self).__init__()
        self.obj_type = 'ContentArea'

class ET_Folder(ET_GetSupport): 
    """
    Wrap an Exact Target DataFolder.
    """
    def __init__(self):
        super(ET_Folder, self).__init__()
        self.obj_type = 'DataFolder'

class ET_BounceEvent(ET_GetSupport):
    """
    Wrap an Exact Target Bounce Event.
    """
    def __init__(self):
        self.obj_type = 'BounceEvent'
     
class ET_Campaign(ET_GetSupportRest):
    """
    Wrap an Exact Target Campaign and associated Assets.
    """
    def __init__(self):
        super(ET_Campaign, self).__init__()
        self.path = '/hub/v1/campaigns/{id}'
        self.urlProps = ["id"]
        self.urlPropsRequired = []
    
class ET_Campaign_Asset(ET_GetSupportRest):
    """
    Wrap an Exact Target Campaign and associated Assets.
    """
    def __init__(self):
        super(ET_Campaign_Asset, self).__init__()
        self.path = '/hub/v1/campaigns/{id}/assets/{assetId}'
        self.urlProps = ["id", "assetId"]
        self.urlPropsRequired = ["id"]
        
class ET_ClickEvent(ET_GetSupport):
    """
    Wrap an Exact Target Click Event.
    """
    def __init__(self):
        super(ET_ClickEvent, self).__init__()
        self.obj_type = 'ClickEvent'
        
class ET_Group(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_Group, self).__init__()
        self.obj_type = 'Group'

class ET_Send(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_Send, self).__init__()
        self.obj_type = 'Send'

class ET_ListSend(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_ListSend, self).__init__()
        self.obj_type = 'ListSend'

class ET_List(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_List, self).__init__()
        self.obj_type = 'List'

class ET_List_Subscriber(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_List_Subscriber, self).__init__()
        self.obj_type = 'ListSubscriber'

class ET_SubscriberList(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_SubscriberList, self).__init__()
        self.obj_type = 'SubscriberList'

class ET_SentEvent(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_SentEvent, self).__init__()
        self.obj_type = 'SentEvent'

class ET_OpenEvent(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_OpenEvent, self).__init__()
        self.obj_type = 'OpenEvent'

class ET_UnsubEvent(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_UnsubEvent, self).__init__()
        self.obj_type = 'UnsubEvent'

class ET_Email(ET_GetSupport):
    """
    Wrap an Exact Target List and List Subscriber.
    """
    def __init__(self):
        super(ET_Email, self).__init__()
        self.obj_type = 'Email'

class ET_TriggeredSend(ET_GetSupport):
    subscribers = None
    attributes  = None
    def __init__(self):
        super(ET_TriggeredSend, self).__init__()
        self.obj_type = 'TriggeredSendDefinition'


class ET_Subscriber(ET_GetSupport):
    def __init__(self):
        super(ET_Subscriber, self).__init__()
        self.obj_type = 'Subscriber'
        
class ET_DataExtension(ET_GetSupport):
    columns = None
    
    def __init__(self):
        super(ET_DataExtension, self).__init__()
        self.obj_type = 'DataExtension' 

class ET_DataExtension_Column(ET_GetSupport):
    def __init__(self):
        super(ET_DataExtension_Column, self).__init__()
        self.obj = 'DataExtensionField'
        
    def get(self):
        '''
        if props and props.is_a? Array then
            @props = props
        end
        '''
        
        if self.props is not None and type(self.props) is dict:
            self.props = self.props.keys()

        '''
        if filter and filter.is_a? Hash then
            @filter = filter
        end
        '''
                
        '''             
        fixCustomerKey = False
        if filter and filter.is_a? Hash then
            @filter = filter
            if @filter.has_key?("Property") && @filter["Property"] == "CustomerKey" then
                @filter["Property"]  = "DataExtension.CustomerKey"
                fixCustomerKey = true 
            end 
        end
        '''
        
        obj = ET_Get(self.auth_stub, self.obj, self.props, self.search_filter)                      
        self.last_request_id = obj.request_id   
        
        ''' 
        if fixCustomerKey then
            @filter["Property"] = "CustomerKey"
        end 
        '''
            
        return obj

class ET_DataExtension_Row(ET_GetSupport):
    Name = None
    CustomerKey = None      
                
    def __init__(self):                             
        super(ET_DataExtension_Row, self).__init__()
        self.obj_type = "DataExtensionObject"
        
    def get(self):
        self.getName()
        '''
        if props and props.is_a? Array then
            @props = props
        end
        '''
        
        if self.props is not None and type(self.props) is dict:
            self.props = self.props.keys()

        '''
        if filter and filter.is_a? Hash then
            @filter = filter
        end
        '''
            
        obj = ET_Get(self.auth_stub, "DataExtensionObject[{0}]".format(self.Name), self.props, self.search_filter)                      
        self.last_request_id = obj.request_id               
            
        return obj
        
    def getName(self):
        if self.Name is None:
            if self.CustomerKey is None:
                raise Exception('Unable to process DataExtension::Row request due to CustomerKey and Name not being defined on ET_DatExtension::row')   
            else:
                de = ET_DataExtension()
                de.auth_stub = self.auth_stub
                de.props = ["Name","CustomerKey"]
                de.search_filter = {'Property' : 'CustomerKey','SimpleOperator' : 'equals','Value' : self.CustomerKey}
                getResponse = de.get()
                if getResponse.status and len(getResponse.results) == 1 and 'Name' in getResponse.results[0]: 
                    self.Name = getResponse.results[0]['Name']
                else:
                    raise Exception('Unable to process DataExtension::Row request due to unable to find DataExtension based on CustomerKey')
