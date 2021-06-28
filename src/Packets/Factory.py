from Packets.Messages.Client.ClientHello import ClientHello
from Packets.Messages.Client.LoginMessage import LoginMessage
from Packets.Messages.Client.KeepAlive import KeepAlive
from Packets.Messages.Client.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.AnalyticsEvent import AnalyticsEvent
from Packets.Messages.Client.SetName import SetName
from Packets.Messages.Client.EndClientTurnMessage import EndClientTurn
from Packets.Messages.Client.TeamChangeBrawlerMessage import TeamChangeBrawlerMessage
from Packets.Messages.Client.TeamSetLocationMessage import TeamSetLocationMessage

packets = {
    10100: ClientHello,
    10101: LoginMessage,
    10108: KeepAlive,
    10110: AnalyticsEvent,
    10212: SetName,
    14102: EndClientTurn,
    14109: GoHomeFromOfflinePractiseMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeBrawlerMessage,
    14363: TeamSetLocationMessage,
}
