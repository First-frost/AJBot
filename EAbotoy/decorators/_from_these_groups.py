from EAbotoy.model import WeChatMsg


def from_these_groups(*groups):
    """只接受这些群组的消息 GroupMsg"""

    def deco(func):
        def inner(ctx: WeChatMsg):
            nonlocal groups

            from_group = ctx.FromUserName
            if from_group in groups:
                return func(ctx)
            return None

        return inner

    return deco
