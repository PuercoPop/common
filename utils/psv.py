from django.conf import settings

def psv_get(request, var_name, default_value=None):                                  
   if settings.PSV_DICT_NAME in request.session and \
    var_name in request.session[settings.PSV_DICT_NAME]:             
        return request.session[settings.PSV_DICT_NAME][var_name]       
   else:                                                                        
        return default_value                                                    
                                                                                
def psv_set(request, var_name, value):                                          
    if settings.PSV_DICT_NAME in request.session:                      
        pass                                                                    
    else:                                                                       
        request.session[settings.PSV_DICT_NAME]={}                     
    request.session[settings.PSV_DICT_NAME][var_name] = value          
    request.session.save()
    return value

def psv_exists(request, var_name):                                              
    if settings.PSV_DICT_NAME in request.session:                      
        return var_name in request.session[settings.PSV_DICT_NAME]     
    else:                                                                       
        return False                                                            

def psv_unset(request, var_name):                                                                                
    if (settings.PSV_DICT_NAME in request.session) and \
        (var_name in request.session[settings.PSV_DICT_NAME]):
        del(request.session[settings.PSV_DICT_NAME][var_name])
    request.session.save()
                                                                                
def psv_save(request):                                                          
    if settings.PSV_DICT_NAME in request.session:                      
        return request.session[settings.PSV_DICT_NAME]                 
                                                                                
    else:                                                                       
        return {}                                                               
                                                                                
def psv_restore(request, new_dict):                                             
    request.session[settings.PSV_DICT_NAME] = new_dict

def psv_destroy(request):
    if settings.PSV_DICT_NAME in request.session:
        del(request.session[settings.PSV_DICT_NAME])
