

class mcq:

  def __init__(self,q,opts,ans):

    """
    multiple choice question

    q -> question str
    opts --> list of options
    ans --> int index of answer
    """
    
    self.q = q
    self.opts = opts
    self.ans = ans

    if type(ans) == type(int):
        self.answer = opts[ans]
    elif type(ans) == type('') and ans in opts:

        self.ans = opts.index(ans)
        self.answer = ans 

    else:
      self.answer = None

  def show(self):
        
    """
    show question + options 
    """
    
    print(self.q,'\n')

    for sn,op in zip(range(1,len(self.opts)+1),self.opts) :
        
        print(f'{sn}: {op}')
   
    print(end='\n')


  def check(self, g_ans):

    """
    checks g_ans with answer
    """

    try:
      if g_ans == self.answer:
        return True

      else:
        return False

    except:

      try:
        return self.answer
      except Exception as e:
        return e

  def __str__(self):

    return self.q











