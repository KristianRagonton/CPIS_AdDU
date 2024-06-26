import { HiOutlineSearch } from "react-icons/hi";
import Avatar from "../Avatars/Avatar";
import { Fragment } from 'react'
import { Menu, Transition } from '@headlessui/react'
import { Link } from "react-router-dom";

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

export default function Header() {
  return (
    <div className='bg-white h-16 px-4 flex justify-between items-center border-b border-gray-200'>
        <div className='relative'>
            <HiOutlineSearch fontSize={20} className='absolute top-1/2 -translate-y-1/2 left-3 text-gray-400'/>
            <input 
                type="text" 
                placeholder='Search...' 
                className="text-sm focus:outline-none active:outline-none h-10  w-[24rem] border border-gray-300 round-sm px-4 pl-10 rounded-3xl">
            </input>
        </div>

        <div>
        <Menu as="div" className="relative inline-block text-left">
          <div>
            <Menu.Button>
              <Avatar imageURL="https://source.unsplash.com/80x80?face" />
            </Menu.Button>
          </div>

          <Transition
            as={Fragment}
            enter="transition ease-out duration-100"
            enterFrom="transform opacity-0 scale-95"
            enterTo="transform opacity-100 scale-100"
            leave="transition ease-in duration-75"
            leaveFrom="transform opacity-100 scale-100"
            leaveTo="transform opacity-0 scale-95"
          >
            <Menu.Items className="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
              <div className="py-1">
                <Link to="/user">
                  <Menu.Item>
                    {({ active }) => (
                      <a
                        href="#"
                        className={classNames(
                          active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                          'block px-4 py-2 text-sm'
                        )}
                      >
                        Profile
                      </a>
                    )}
                  </Menu.Item>
                </Link>
                <Link to="/Logout">
                  <Menu.Item>
                    {({ active }) => (
                      <button
                        type="submit"
                        className={classNames(
                          active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                          'block w-full px-4 py-2 text-left text-sm'
                        )}
                      >
                        Log out
                      </button>
                    )}
                  </Menu.Item>
                </Link>
              </div>
            </Menu.Items>
          </Transition>
        </Menu>
        </div>
    </div>
  )
}
