from rest_framework.routers import DefaultRouter
from ..category.views import CategoryViewset
from ..product.views import ProductsViewset
from ..productCategory.views import productCategoryViewset
from ..store.views import StoreViewset

router = DefaultRouter()

router.register(r'category',CategoryViewset, basename='category')
router.register(r'product', ProductsViewset, basename='product')
router.register(r'productCategory', productCategoryViewset, basename='productCategory')
router.register(r'store', StoreViewset, basename='store')

urlpatterns = router.urls