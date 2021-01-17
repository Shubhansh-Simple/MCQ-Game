import matplotlib.pyplot as plt
import base64
from   io    import BytesIO
import numpy as     np

def get_graph():
    '''Do some buffer reading,encoding-decoding stuff'''

    img_buffer = BytesIO()
    plt.savefig( img_buffer,format='png' )
    img_buffer.seek(0)
    img_png    = img_buffer.getvalue()
    graph      = base64.b64encode( img_png )
    graph      = graph.decode('utf-8')

    img_buffer.close()

    return graph

def get_plot( correct_answers,skip_questions,username ):
    '''Entire matplotlib code shape colour etc.'''

    plt.switch_backend('AGG')
    plt.title('Contestent Performance.')
    plt.ylabel('No of questions')
    plt.xlabel('Users')
    #plt.figure(figsize=(20, 15))
    
    index = np.arange( len( correct_answers ) )
    width = 0.50
    
    plt.bar( index,
             correct_answers,width,
             color='green',
             align='edge',
             label='Right Answers' )

    plt.bar( index+width,
             skip_questions,
             width-0.10,
             color='red',
             align='edge',
             label='Skip Questions' )
    
    #plt.tight_layout()
    plt.legend( loc='upper right')
    plt.xticks( index+width,username )

    graph = get_graph()
    return graph


