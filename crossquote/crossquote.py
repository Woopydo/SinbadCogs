import os
import sys
import asyncio
import discord
import logging
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks

log = logging.getLogger('red.CrossQuote')

class CrossQuote:
    """
    Cross server quote by message ID. Formatting of the embed was taken from
    https://github.com/PaddoInWonderland/PaddoCogs/quote/quote.py
    For the sake of privacy, allowing a quote from another server will require
    that the user attempting to quote from that server can manage messages or
    that someone who can manage server has disabled this check for their server.
    """ #Yes, I am aware you can still copy/paste manually if you can see the ID

    def __init__(self, bot):
        self.bot = bot

        __version__ = "0.2self"
        self.bot = bot

    @commands.command(pass_context=True, name='crossquote', aliases=['q','quote'])
    async def _q(self, ctx, message_id: int):
        """
        Quote someone with the message id. To get the message id you need to enable developer mode.
        """
        found = False
        for server in self.bot.servers:
            for channel in server.channels:
                if not found:
                    try:
                        message = await self.bot.get_message(channel, str(message_id))
                        if message:
                            await self.sendifallowed(ctx.message.channel, message)
                    except Exception as error:
                        log.debug(error)



    async def sendifallowed(self, where, message=None):
        "checks if a response should be sent, then sends the appropriate response"

        if message:
            channel = message.channel
            server = channel.server
            content = message.clean_content
            author = message.author
            sname = server.name
            cname = channel.name
            timestamp = message.timestamp.strftime('%Y-%m-%d %H:%M')
            avatar = author.avatar_url if author.avatar else author.default_avatar_url
            footer = 'Said in {} #{} at {}'.format(sname, cname, timestamp)
            em = discord.Embed(description=content, color=discord.Color.purple())
            em.set_author(name='{}'.format(author.name), icon_url=avatar)
            em.set_footer(text=footer)
            await self.bot.send_message(where, embed=em)
        else:
            em = log.debug("no such message")


def setup(bot):
    n = CrossQuote(bot)
    bot.add_cog(n)
