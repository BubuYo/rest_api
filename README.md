# rest_api
Blog api based on Django 1.9 and django rest framework3.5.4
# 初版：

- 实现三个并列的 article tag comment 的api，可以新增和列表。
- 登录功能
- 序列化和反序列化
- api权限设置为管理员（不科学,已修改
- api分页（10个每页）


# 已补充：
- 补充实现article增删改查
- views中的多行注释可以出现在网页上
- 新的权限处理方法：

        views中使用
        from rest_framework import permissions
        并在comment类中添加
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        来实现已验证的请求获得读写访问，未经验证的请求获得只读访问
        article类和tag类使用admin权限

# 待补充：
- api请求速率限制
- 数据校验
- Debug = false
- api网址加？不识别
- 使用from django.test import TestCase 进行单元测试
- tag和comment的article_id改为article-id,增加可读性


# 使用
## 我们可以通过使用Accept header来控制回传的格式。

http://127.0.0.1:8000/articles/ Accept:application/json  # 请求 JSON
http://127.0.0.1:8000/articles/ Accept:text/html         # 请求 HTML
## 或者直接附加一个格式后缀

http://127.0.0.1:8000/articles.json  # JSON 后缀
http://127.0.0.1:8000/articles.api   # 可浏览的 API 后缀
## 同样，我们可以使用Content-Type头来控制我们发送的请求的格式。

## 使用表单POST数据
curl -X POST -d tag=api -d article_id=1 -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/tags/

## 使用JSON来POST数据
http --json POST http://127.0.0.1:8000/tags/ tag="lucky" article_id=1

{
    "id": 4,
    "title": "",
    "code": "print 456",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}
##如果你在上述的HTTP请求中加一个--debug，你将看到请求的类型在请求头里