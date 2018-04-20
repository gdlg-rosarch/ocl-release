/***************************************************************************
  tag: Peter Soetens  Thu Apr 22 20:40:58 CEST 2004  EmptyHeaderMarshaller.hpp

                        EmptyHeaderMarshaller.hpp -  description
                           -------------------
    begin                : Thu April 22 2004
    copyright            : (C) 2004 Peter Soetens
    email                : peter.soetens@mech.kuleuven.ac.be

 ***************************************************************************
 *   This library is free software; you can redistribute it and/or         *
 *   modify it under the terms of the GNU General Public                   *
 *   License as published by the Free Software Foundation;                 *
 *   version 2 of the License.                                             *
 *                                                                         *
 *   As a special exception, you may use this file as part of a free       *
 *   software library without restriction.  Specifically, if other files   *
 *   instantiate templates or use macros or inline functions from this     *
 *   file, or you compile this file and link it with other files to        *
 *   produce an executable, this file does not by itself cause the         *
 *   resulting executable to be covered by the GNU General Public          *
 *   License.  This exception does not however invalidate any other        *
 *   reasons why the executable file might be covered by the GNU General   *
 *   Public License.                                                       *
 *                                                                         *
 *   This library is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU     *
 *   Lesser General Public License for more details.                       *
 *                                                                         *
 *   You should have received a copy of the GNU General Public             *
 *   License along with this library; if not, write to the Free Software   *
 *   Foundation, Inc., 59 Temple Place,                                    *
 *   Suite 330, Boston, MA  02111-1307  USA                                *
 *                                                                         *
 ***************************************************************************/


#ifndef PI_PROPERTIES_EMPTYHEADER_SERIALIZER
#define PI_PROPERTIES_EMPTYHEADER_SERIALIZER

#include <rtt/Property.hpp>
#include <rtt/base/PropertyIntrospection.hpp>
#include <rtt/marsh/StreamProcessor.hpp>

namespace RTT
{
    /**
     * @brief A Dummy Empty Header MarshallInterface.
     */
    template<typename o_stream>
    class EmptyHeaderMarshaller
        : public marsh::MarshallInterface,
          public marsh::StreamProcessor<o_stream>
    {
    public:
        typedef o_stream output_stream;
        typedef o_stream OutputStream;

        EmptyHeaderMarshaller(output_stream &os) :
            marsh::StreamProcessor<o_stream>(os)
        {
        }

        virtual ~EmptyHeaderMarshaller() {}

        virtual void flush() {}

        virtual void serialize(base::PropertyBase* v)
        {
        }

        virtual void serialize(const PropertyBag &v)
        {
        }
	};
}
#endif
