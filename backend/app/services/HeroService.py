from ..models import Hero

class HeroService():

  @classmethod 
  def get(self, id):
    return Hero.query.get_or_404(id)

  @classmethod
  def list(self):
    return Hero.query.all()

  @classmethod
  def save(self):
    pass
    
  @classmethod
  def update(self):
    pass