package ch.ethz.systems.netbench.xpt.voijslav_and_sppifo.tcp.buffertcp;


import ch.ethz.systems.netbench.core.network.Socket;
import ch.ethz.systems.netbench.core.network.TransportLayer;
import ch.ethz.systems.netbench.xpt.simple.simpleudp.SimpleUdpSocket;
import ch.ethz.systems.netbench.xpt.voijslav_and_sppifo.tcp.sptcp.SpTcpSocket;

public class BufferTcpTransportLayer extends TransportLayer {

	private long seed;
    /**
     * Create the TCP transport layer with the given network device identifier.
     * The network device identifier is used to create unique flow identifiers.
     *
     * @param identifier        Parent network device identifier
     */
    public BufferTcpTransportLayer(int identifier, long seed) {
        super(identifier);
        this.seed = seed;
    }

    @Override
    protected Socket createSocket(long flowId, int destinationId, long flowSizeByte) {
        return new BufferTcpSocket(this, flowId, this.identifier, destinationId, flowSizeByte, seed);
    }

    @Override
    protected Socket createSocketWithRealFlowSize(long flowId, int destinationId, long flowSizeByte, long realFlowSizeByte) {
        return new BufferTcpSocket(this, flowId, this.identifier, destinationId, flowSizeByte, seed);
    }

    @Override
    protected Socket createSocketWithPort(long flowId, int destinationId, long flowSizeByte, int sourcePort, int destinationPort) {
        return new BufferTcpSocket(this, flowId, this.identifier, destinationId, flowSizeByte, seed);
//        return new DemoSocket(this, flowId, identifier, destinationId, flowSizeByte, sourcePort, destinationPort);
    }

    @Override
    protected Socket createSocketWithPortAndRealFlowSize(long flowId, int destinationId, long flowSizeByte, long realFlowSizeByte, int sourcePort, int destinationPort) {
        if (flowSizeByte == -1) {
            return new SimpleUdpSocket(this, flowId, destinationId, identifier, flowSizeByte, realFlowSizeByte, sourcePort, destinationPort);
        }
        else {
            return new SimpleUdpSocket(this, flowId, identifier, destinationId, flowSizeByte, realFlowSizeByte, sourcePort, destinationPort);
        }
    }
}
